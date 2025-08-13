import os
import sys
import requests
import shutil
from bs4 import BeautifulSoup
from google.cloud import storage
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- CONFIGURAÇÃO ---
BUCKET_NAME = os.environ.get("BUCKET_NAME")
CHROMA_BUCKET_PATH = "chroma_db_ricms"
CHROMA_LOCAL_DIR = "/tmp/chroma_db"
URLS_LEGISLACAO = {
    "regulamento": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_00.htm",
    "anexo_2": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_an_02.htm",
    "anexo_3": "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_an_03.htm",
}

# --- FUNÇÕES AUXILIARES ---
def extrair_texto_sef(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for element in soup(["script", "style", "header", "footer", "nav"]):
            element.decompose()
        return soup.get_text(separator='\n', strip=True)
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return ""

def coletar_toda_legislacao():
    # ESTA É A LINHA CORRIGIDA
    textos =
    for chave, url in URLS_LEGISLACAO.items():
        print(f"Coletando dados de: {chave}")
        texto = extrair_texto_sef(url)
        if texto:
            textos.append(texto)
    return "\n\n--- FIM DA SEÇÃO ---\n\n".join(textos)

# --- PONTO DE ENTRADA PRINCIPAL ---
if __name__ == "__main__":
    if not BUCKET_NAME:
        print("Erro: A variável de ambiente BUCKET_NAME não está definida.")
        sys.exit(1)

    print("Iniciando a atualização da base de dados do RICMS/SC.")

    texto_consolidado = coletar_toda_legislacao()
    if not texto_consolidado:
        print("Falha na coleta dos textos. Abortando.")
        sys.exit(1)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
    docs = text_splitter.create_documents([texto_consolidado])

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    if os.path.exists(CHROMA_LOCAL_DIR):
        shutil.rmtree(CHROMA_LOCAL_DIR)

    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=CHROMA_LOCAL_DIR
    )
    vector_store.persist()
    print("Banco de dados vetorial criado localmente.")

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    for root, _, files in os.walk(CHROMA_LOCAL_DIR):
        for file in files:
            local_path = os.path.join(root, file)
            bucket_path = os.path.join(CHROMA_BUCKET_PATH, os.path.relpath(local_path, CHROMA_LOCAL_DIR))
            blob = bucket.blob(bucket_path)
            blob.upload_from_filename(local_path)

    print("Atualização da base de dados concluída e salva no Cloud Storage.")
