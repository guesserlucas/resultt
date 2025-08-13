import os
import sys
import time
import shutil
import logging
import requests
from bs4 import BeautifulSoup
from google.cloud import storage
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google.api_core.exceptions import ResourceExhausted

# --- CONFIGURAÇÃO DE LOGGING ---
# Configura um logging mais informativo que os prints.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- CONFIGURAÇÃO DE PARÂMETROS ---
# Utiliza variáveis de ambiente para maior flexibilidade.
BUCKET_NAME = os.environ.get("BUCKET_NAME")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY") # A chave da API também deve ser uma variável de ambiente.

# Caminhos para o banco de dados vetorial
CHROMA_BUCKET_PATH = "chroma_db_ricms"
CHROMA_LOCAL_DIR = "/tmp/chroma_db_ricms"

# URLs da legislação a serem processadas
URLS_LEGISLACAO = {
    "regulamento": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_00.htm",
    "anexo_2": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_an_02.htm",
    "anexo_3": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_an_03.htm",
}

# Parâmetros para o processamento de embeddings
EMBEDDING_MODEL = "models/embedding-001"
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200
BATCH_SIZE = 15 # Tamanho seguro do lote para evitar exceder os limites da API.
SECONDS_BETWEEN_BATCHES = 2 # Pausa para respeitar o limite de requisições por minuto.

# --- FUNÇÕES AUXILIARES ---

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
    blobs = bucket.list_blobs(prefix=bucket_path)
    downloaded = False
    for blob in blobs:
        if not blob.name.endswith('/'): # Ignora "pastas"
            destination_uri = os.path.join(local_path, os.path.relpath(blob.name, bucket_path))
            os.makedirs(os.path.dirname(destination_uri), exist_ok=True)
            blob.download_to_filename(destination_uri)
            downloaded = True
    if downloaded:
        logging.info(f"Banco de dados Chroma baixado de gs://{bucket_name}/{bucket_path} para {local_path}")
    else:
        logging.info(f"Nenhum banco de dados Chroma encontrado em gs://{bucket_name}/{bucket_path}")
    return downloaded

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

# Decorador de retentativa para a função de adicionar documentos.
# Tenta 3 vezes com espera exponencial em caso de erro de 'ResourceExhausted'.
@retry(
    wait=wait_exponential(multiplier=1, min=2, max=60),
    stop=stop_after_attempt(3),
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

    logging.info("Iniciando a atualização da base de dados do RICMS/SC.")

    # 1. Coleta e processamento do texto
    texto_consolidado = coletar_toda_legislacao()
    if not texto_consolidado:
        logging.error("Falha na coleta dos textos. Abortando.")
        sys.exit(1)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    docs = text_splitter.create_documents([texto_consolidado])

    # 2. Validação dos dados - remove documentos vazios
    docs_validos = [doc for doc in docs if doc.page_content and not doc.page_content.isspace()]
    logging.info(f"Total de documentos criados: {len(docs)}. Documentos válidos (não vazios): {len(docs_validos)}.")
    if not docs_validos:
        logging.warning("Nenhum documento válido foi gerado após o processamento. Abortando.")
        sys.exit(0)

    # 3. Preparação do ambiente local e do cliente GCS
    if os.path.exists(CHROMA_LOCAL_DIR):
        shutil.rmtree(CHROMA_LOCAL_DIR)
    os.makedirs(CHROMA_LOCAL_DIR)

    storage_client = storage.Client()
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=GOOGLE_API_KEY)
    
    # 4. Carregamento ou criação do banco de dados vetorial (Estratégia Incremental)
    vector_store = None
    if download_chroma_from_gcs(storage_client, BUCKET_NAME, CHROMA_BUCKET_PATH, CHROMA_LOCAL_DIR):
        logging.info("Carregando banco de dados Chroma existente.")
        vector_store = Chroma(persist_directory=CHROMA_LOCAL_DIR, embedding_function=embeddings)
    else:
        logging.info("Criando um novo banco de dados Chroma.")
        # O banco será criado com o primeiro lote de documentos.

    # 5. Processamento em Lotes (Batching) com Rate Limiting e Retries
    total_docs = len(docs_validos)
    for i in range(0, total_docs, BATCH_SIZE):
        batch_start_time = time.time()
        docs_batch = docs_validos
        
        if vector_store is None:
            # Se o vector_store ainda não foi criado, cria com o primeiro lote.
            vector_store = Chroma.from_documents(
                documents=docs_batch,
                embedding=embeddings,
                persist_directory=CHROMA_LOCAL_DIR
            )
            logging.info("Novo banco de dados Chroma inicializado com o primeiro lote.")
        else:
            # Adiciona lotes subsequentes ao banco de dados existente.
            try:
                add_documents_with_retry(vector_store, docs_batch)
            except Exception as e:
                logging.error(f"Falha ao adicionar lote de documentos após múltiplas tentativas: {e}")
                # Decide se deve parar ou continuar, dependendo da criticidade.
                # Neste caso, vamos parar para investigar.
                sys.exit(1)

        # Pausa para respeitar os limites da API
        if i + BATCH_SIZE < total_docs:
            logging.info(f"Lote {i//BATCH_SIZE + 1} processado. Pausando por {SECONDS_BETWEEN_BATCHES} segundos...")
            time.sleep(SECONDS_BETWEEN_BATCHES)

    # 6. Persistência e Upload para o GCS
    logging.info("Persistindo alterações no banco de dados localmente.")
    vector_store.persist()
    
    logging.info("Iniciando upload do banco de dados atualizado para o Cloud Storage.")
    upload_chroma_to_gcs(storage_client, BUCKET_NAME, CHROMA_LOCAL_DIR, CHROMA_BUCKET_PATH)

    logging.info("Atualização da base de dados concluída com sucesso.")
