#Otto P. S. Guesser
import os
import sys
import shutil
import asyncio
import functions_framework
from google.cloud import storage
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    # Esta verificação irá logar um erro crítico e causar a saída do contêiner
    # na inicialização se a variável GOOGLE_API_KEY não estiver definida,
    # impedindo que uma revisão quebrada seja implantada com sucesso.
    print("ERRO FATAL: A variável de ambiente GOOGLE_API_KEY não foi definida.", file=sys.stderr)
    sys.exit(1)

# --- CONFIGURAÇÃO GLOBAL ---
BUCKET_NAME = os.environ.get("BUCKET_NAME")
CHROMA_BUCKET_PATH = "chroma_db_ricms"
CHROMA_LOCAL_DIR = "/tmp/chroma_db"

# --- ESTADO GLOBAL ---
qa_chain = None

async def _initialize_async():
    """
    Função assíncrona que contém a lógica de inicialização real.
    """
    global qa_chain
    
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
    print("INFO: Carregando modelos e preparando a cadeia de QA...")

    # --- LOGS DE DIAGNÓSTICO ---
    print("DEBUG: Criando GoogleGenerativeAIEmbeddings...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    print("DEBUG: GoogleGenerativeAIEmbeddings criado com sucesso.")

    print("DEBUG: Criando Chroma vector store...")
    vector_store = Chroma(persist_directory=CHROMA_LOCAL_DIR, embedding_function=embeddings)
    print("DEBUG: Chroma vector store criado com sucesso.")

    print("DEBUG: Criando ChatGoogleGenerativeAI...")
    # Linha Corrigida
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
    print("DEBUG: ChatGoogleGenerativeAI criado com sucesso.")
    # --- FIM DOS LOGS DE DIAGNÓSTICO ---

    prompt_template = """
    Contexto:
    {context}
    Faça levantamento sobre o item "{question}" e busque informações complementares sobre ele, como NCM, descrição completa, variações etc então baseando-se EXCLUSIVAMENTE no contexto fornecido acima forneça um resumo detalhado e claro do tratamento tributário para o item.

                    O resumo deve obrigatoriamente incluir os seguintes pontos, quando aplicáveis:

                    1.  **Alíquota Interna:** Qual a alíquota padrão de ICMS para este produto em operações dentro de SC?
                    2.  **Substituição Tributária (ICMS-ST):** O produto está sujeito ao regime de ST? Se sim, mencione o MVA/IVA-ST aplicável (original e ajustado para 4% e 12%, se houver) e a base legal (dispositivo do RICMS/SC).
                    3.  **Isenção:** Existe alguma isenção de ICMS para este produto? Se sim, qual e sob quais condições? Citar a base legal.
                    4.  **Redução de Base de Cálculo:** Há alguma redução na base de cálculo do ICMS? Se sim, qual o percentual e as condições? Citar a base legal.
                    5.  **Crédito Presumido:** Existe algum benefício de crédito presumido? Se sim, qual o percentual e para qual tipo de empresa/operação se aplica? Citar a base legal.
                    6.  **Observações Importantes:** Qualquer outra informação relevante, como regimes especiais, diferimento, ou particularidades da operação.

                    Formate a resposta usando Markdown, com títulos claros para cada seção (ex: ## Alíquota, ## Substituição Tributária).
                    Se o NCM não for encontrado ou a descrição for muito genérica, informe que não foi possível localizar uma tributação específica e peça mais detalhes.
                    Aja como um consultor tributário especialista em legislação catarinense.

    """
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    print("INFO: Inicialização do worker concluída com sucesso.")

def initialize_worker_state():
    """
    Invólucro síncrono para executar a inicialização assíncrona.
    """
    global qa_chain
    try:
        print("INFO: Iniciando estado para um novo worker (lazy initialization)...")
        asyncio.run(_initialize_async())
    except Exception as e:
        print(f"ERRO FATAL durante a inicialização do worker: {e}")
        qa_chain = None

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
        if qa_chain is None:
            initialize_worker_state()
        
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
