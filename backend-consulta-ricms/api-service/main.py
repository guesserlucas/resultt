import os
import shutil
import asyncio
import functions_framework
from google.cloud import storage
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- CONFIGURAÇÃO GLOBAL ---
BUCKET_NAME = os.environ.get("BUCKET_NAME")
CHROMA_BUCKET_PATH = "chroma_db_ricms"
CHROMA_LOCAL_DIR = "/tmp/chroma_db"

# --- ESTADO GLOBAL (CACHE EM NÍVEL DE INSTÂNCIA) ---
# PASSO 1: Inicialize a variável global como None.
# Ela será preenchida por cada worker na sua primeira requisição.
qa_chain = None

def initialize_worker_state():
    """
    Função para inicializar o estado para um worker específico.
    Esta função será chamada de forma "preguiçosa" (lazy) na primeira
    requisição que um worker receber.
    """
    # Usamos 'global' para modificar a variável no escopo do módulo.
    global qa_chain
    
    try:
        print("INFO: Inicializando estado para um novo worker (lazy initialization)...")
        
        # 1. Baixar o banco de dados do GCS
        print(f"INFO: Baixando banco de dados de gs://{BUCKET_NAME}/{CHROMA_BUCKET_PATH}...")
        storage_client = storage.Client()
        
        if os.path.exists(CHROMA_LOCAL_DIR):
            shutil.rmtree(CHROMA_LOCAL_DIR)
        os.makedirs(CHROMA_LOCAL_DIR, exist_ok=True)

        bucket = storage_client.bucket(BUCKET_NAME)
        blobs = list(storage_client.list_blobs(BUCKET_NAME, prefix=CHROMA_BUCKET_PATH))
        
        if not blobs:
            raise FileNotFoundError(f"Nenhum arquivo de banco de dados vetorial encontrado em gs://{BUCKET_NAME}/{CHROMA_BUCKET_PATH}.")

        for blob in blobs:
            if not blob.name.endswith('/'):
                destination_file_name = os.path.join(CHROMA_LOCAL_DIR, os.path.relpath(blob.name, CHROMA_BUCKET_PATH))
                os.makedirs(os.path.dirname(destination_file_name), exist_ok=True)
                blob.download_to_filename(destination_file_name)
        
        print("INFO: Download concluído.")

        # 2. Inicializar os componentes do LangChain
        print("INFO: Carregando modelos e preparando a cadeia de QA...")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = Chroma(persist_directory=CHROMA_LOCAL_DIR, embedding_function=embeddings)
        llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1)

        prompt_template = """
        Aja como um consultor tributário especialista em legislação de ICMS de Santa Catarina.
        Baseando-se EXCLUSIVAMENTE no contexto fornecido abaixo, responda à pergunta do usuário.
        Se a informação não estiver no contexto, informe claramente: "A informação sobre '{question}' não foi encontrada na legislação consultada."
        Contexto:
        {context}

        Pergunta do usuário: "{question}"

        Forneça uma resposta completa e bem estruturada em Markdown.
        """
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

        # 3. Montar e atribuir a cadeia de QA à variável global
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
            chain_type_kwargs={"prompt": PROMPT}
        )
        
        print("INFO: Inicialização do worker concluída com sucesso.")

    except Exception as e:
        print(f"ERRO FATAL durante a inicialização do worker: {e}")
        # Deixar qa_chain como None para que futuras requisições a este worker falhem rapidamente.
        qa_chain = None

# --- PONTO DE ENTRADA (ENTRY POINT) ---
@functions_framework.http
def executar_consulta(request):
    global qa_chain
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    if request.method == 'OPTIONS':
        return ('', 204, headers)

    try:
        # PASSO 2: Implementar a lógica de inicialização lenta.
        # Esta verificação garante que a inicialização ocorra apenas uma vez por worker.
        if qa_chain is None:
            initialize_worker_state()
        
        # Se a inicialização falhou, qa_chain ainda será None.
        if qa_chain is None:
            raise RuntimeError("O serviço não está disponível devido a um erro de inicialização do worker.")

        request_json = request.get_json(force=True)
        query = request_json.get("query")
        if not query:
            raise ValueError("O campo 'query' é obrigatório no corpo do JSON.")

        async def _get_qa_response_async(user_query):
            resultado_dict = await qa_chain.ainvoke({"query": user_query})
            return resultado_dict.get("result", "Não foi possível obter uma resposta.")

        resultado = asyncio.run(_get_qa_response_async(query))
        
        return ({"resposta": resultado}, 200, headers)

    except ValueError as e:
        return ({"error": f"Requisição inválida: {e}"}, 400, headers)
    except Exception as e:
        print(f"Erro interno ao processar a consulta: {e}")
        return ({"error": "Ocorreu um erro interno ao processar sua solicitação."}, 500, headers)
