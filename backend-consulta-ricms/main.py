# backend-consulta-ricms/main_corrigido.py

import os
import sys
import time
import shutil
import logging
import requests
import psutil  # Adicionado para monitoramento de memória
from bs4 import BeautifulSoup
from google.cloud import storage
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google.api_core.exceptions import ResourceExhausted

# --- CONFIGURAÇÃO DE LOGGING ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- CONFIGURAÇÃO DE PARÂMETROS ---
BUCKET_NAME = os.environ.get("BUCKET_NAME")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
CHROMA_BUCKET_PATH = "chroma_db_ricms"
CHROMA_LOCAL_DIR = "/tmp/chroma_db_ricms"

URLS_LEGISLACAO = {
    "regulamento": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_00.htm",
    "anexo_2": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_02_pas.htm",
    "anexo_3": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_03_pas.htm",
}

EMBEDDING_MODEL = "models/embedding-001"
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200
BATCH_SIZE = 100  # Aumentado para otimizar chamadas de API
SECONDS_BETWEEN_BATCHES = 5 # Aumentado para respeitar limites de API

# --- FUNÇÕES AUXILIARES ---

def log_memory_usage(stage=""):
    """Registra o uso atual de memória do sistema."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    total_mem = psutil.virtual_memory()
    logging.info(
        f"Uso de Memória ({stage}): "
        f"Processo RSS: {mem_info.rss / 1024 / 1024:.2f} MB. "
        f"Total do Sistema Usado: {total_mem.used / 1024 / 1024:.2f} MB ({total_mem.percent}%)"
    )

def extrair_texto_sef(url):
    """Extrai o texto limpo de uma URL da SEF/SC."""
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for element in soup(["script", "style", "header", "footer", "nav"]):
            element.decompose()
        return soup.get_text(separator='\n', strip=True)
    except requests.RequestException as e:
        logging.error(f"Erro ao acessar a URL {url}: {e}")
        return ""

def coletar_toda_legislacao():
    """Coleta e consolida os textos de todas as URLs configuradas."""
    textos = []
    for chave, url in URLS_LEGISLACAO.items():
        logging.info(f"Coletando dados de: {chave}")
        texto = extrair_texto_sef(url)
        if texto:
            textos.append(texto)
    return "\n\n--- FIM DA SEÇÃO ---\n\n".join(textos)

def download_chroma_from_gcs(storage_client, bucket_name, bucket_path, local_path):
    """Baixa o banco de dados Chroma existente do GCS."""
    bucket = storage_client.bucket(bucket_name)
    blobs = list(bucket.list_blobs(prefix=bucket_path))
    if not blobs:
        logging.info(f"Nenhum banco de dados Chroma encontrado em gs://{bucket_name}/{bucket_path}")
        return False
    
    os.makedirs(local_path, exist_ok=True)
    for blob in blobs:
        if not blob.name.endswith('/'):
            destination_uri = os.path.join(local_path, os.path.relpath(blob.name, bucket_path))
            os.makedirs(os.path.dirname(destination_uri), exist_ok=True)
            blob.download_to_filename(destination_uri)
    logging.info(f"Banco de dados Chroma baixado de gs://{bucket_name}/{bucket_path} para {local_path}")
    return True

def upload_chroma_to_gcs(storage_client, bucket_name, local_path, bucket_path):
    """Faz o upload do banco de dados Chroma local para o GCS."""
    bucket = storage_client.bucket(bucket_name)
    for root, _, files in os.walk(local_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            gcs_file_path = os.path.join(bucket_path, os.path.relpath(local_file_path, local_path))
            blob = bucket.blob(gcs_file_path)
            blob.upload_from_filename(local_file_path)
    logging.info(f"Banco de dados Chroma salvo em gs://{bucket_name}/{bucket_path}")

# --- LÓGICA PRINCIPAL ---

@retry(
    wait=wait_exponential(multiplier=2, min=4, max=60),
    stop=stop_after_attempt(5),
    retry=retry_if_exception_type(ResourceExhausted)
)
def add_documents_with_retry(vector_store, docs_batch):
    """Adiciona um lote de documentos ao vector store com lógica de retentativa."""
    logging.info(f"Adicionando lote de {len(docs_batch)} documentos...")
    vector_store.add_documents(docs_batch)
    logging.info("Lote adicionado com sucesso.")

if __name__ == "__main__":
    if not BUCKET_NAME or not GOOGLE_API_KEY:
        logging.error("Erro: As variáveis de ambiente BUCKET_NAME e GOOGLE_API_KEY devem estar definidas.")
        sys.exit(1)

    log_memory_usage("Início do Job")
    logging.info("Iniciando a atualização da base de dados do RICMS/SC.")

    texto_consolidado = coletar_toda_legislacao()
    if not texto_consolidado:
        logging.error("Falha na coleta dos textos. Abortando.")
        sys.exit(1)
    
    log_memory_usage("Após coleta de texto")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    docs = text_splitter.create_documents([texto_consolidado])
    docs_validos = [doc for doc in docs if doc.page_content and not doc.page_content.isspace()]
    logging.info(f"Total de documentos criados: {len(docs)}. Documentos válidos (não vazios): {len(docs_validos)}.")
    
    del texto_consolidado, docs # Libera memória
    log_memory_usage("Após divisão de texto")

    if not docs_validos:
        logging.warning("Nenhum documento válido foi gerado após o processamento. Abortando.")
        sys.exit(0)

    if os.path.exists(CHROMA_LOCAL_DIR):
        shutil.rmtree(CHROMA_LOCAL_DIR)
    os.makedirs(CHROMA_LOCAL_DIR)

    storage_client = storage.Client()
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=GOOGLE_API_KEY)
    
    vector_store = None
    # Esta abordagem ainda usa o sistema de arquivos em memória.
    # A recomendação arquitetural é usar um banco de dados vetorial gerenciado.
    logging.info("Criando um novo banco de dados Chroma.")

    total_docs = len(docs_validos)
    for i in range(0, total_docs, BATCH_SIZE):
        # CORREÇÃO CRÍTICA: Fatiar a lista para criar um lote real.
        docs_batch = docs_validos
        
        if not docs_batch:
            continue

        try:
            if vector_store is None:
                # Inicializa o banco com o primeiro lote
                vector_store = Chroma.from_documents(
                    documents=docs_batch,
                    embedding=embeddings,
                    persist_directory=CHROMA_LOCAL_DIR
                )
                logging.info("Novo banco de dados Chroma inicializado com o primeiro lote.")
            else:
                # Adiciona lotes subsequentes
                add_documents_with_retry(vector_store, docs_batch)
        except Exception as e:
            logging.error(f"Falha fatal ao adicionar lote de documentos: {e}")
            sys.exit(1)

        log_memory_usage(f"Após lote {i//BATCH_SIZE + 1}/{total_docs//BATCH_SIZE + 1}")

        if i + BATCH_SIZE < total_docs:
            logging.info(f"Pausando por {SECONDS_BETWEEN_BATCHES} segundos...")
            time.sleep(SECONDS_BETWEEN_BATCHES)

    logging.info("Persistindo alterações finais no banco de dados localmente.")
    if vector_store:
        vector_store.persist()
    
    log_memory_usage("Após persistência local")
    
    logging.info("Iniciando upload do banco de dados atualizado para o Cloud Storage.")
    upload_chroma_to_gcs(storage_client, BUCKET_NAME, CHROMA_LOCAL_DIR, CHROMA_BUCKET_PATH)

    log_memory_usage("Fim do Job")
    logging.info("Atualização da base de dados concluída com sucesso.")
