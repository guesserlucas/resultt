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
# Estas variáveis serão inicializadas UMA VEZ por instância do contêiner.
# Elas são definidas como None inicialmente.
qa_chain = None

def initialize_global_state():
    """
    Função para inicializar o estado global. Baixa o DB do GCS, carrega os modelos
    e prepara a cadeia de QA. Executada apenas uma vez quando a instância do 
    contêiner inicia (cold start).
    """
    global qa_chain
    
    # Impede a re-inicialização se a função for chamada acidentalmente de novo.
    if qa_chain is not None:
        print("INFO: Estado global já inicializado.")
        return

    try:
        print("INFO: Iniciando inicialização do estado global (cold start)...")
        
        # 1. Baixar o banco de dados do GCS (lógica movida para cá)
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

        # 2. Inicializar os componentes do LangChain (lógica movida para cá)
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

        # 3. Montar e armazenar a cadeia de QA na variável global
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
            chain_type_kwargs={"prompt": PROMPT}
        )
        
        print("INFO: Inicialização do estado global concluída com sucesso.")

    except Exception as e:
        # Se a inicialização falhar, registramos o erro. As requisições subsequentes falharão rapidamente.
        print(f"ERRO FATAL durante a inicialização: {e}")
        qa_chain = None # Garante que permaneça None em caso de falha

# --- EXECUÇÃO DA INICIALIZAÇÃO ---
# Chame a função aqui, no escopo global. O código neste escopo é executado
# automaticamente quando uma nova instância do Cloud Run é criada.
initialize_global_state()

# --- PONTO DE ENTRADA (ENTRY POINT) ---
@functions_framework.http
def executar_consulta(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    if request.method == 'OPTIONS':
        return ('', 204, headers)

    try:
        # Etapa de inicialização foi removida daqui. Agora apenas processamos a requisição.
        
        # Verifica se a inicialização global falhou.
        if qa_chain is None:
            print("ERRO: O serviço não foi inicializado corretamente. Verifique os logs de inicialização da instância.")
            raise RuntimeError("O serviço não está disponível devido a um erro de inicialização.")

        request_json = request.get_json(force=True)
        query = request_json.get("query")
        if not query:
            raise ValueError("O campo 'query' é obrigatório no corpo do JSON.")

        # Função assíncrona interna para executar a consulta usando a cadeia global
        async def _get_qa_response_async(user_query):
            # A chamada assíncrona real acontece aqui, usando a `qa_chain` pré-carregada
            resultado_dict = await qa_chain.ainvoke({"query": user_query})
            return resultado_dict.get("result", "Não foi possível obter uma resposta.")

        # Chama a função assíncrona a partir do contexto síncrono
        resultado = asyncio.run(_get_qa_response_async(query))
        
        return ({"resposta": resultado}, 200, headers)

    except ValueError as e:
        return ({"error": f"Requisição inválida: {e}"}, 400, headers)
    except Exception as e:
        print(f"Erro interno ao processar a consulta: {e}")
        return ({"error": "Ocorreu um erro interno ao processar sua solicitação."}, 500, headers)
