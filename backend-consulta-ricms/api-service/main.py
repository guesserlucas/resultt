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

# --- VERIFICAÇÃO DE VARIÁVEL DE AMBIENTE ---
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
# A cadeia de QA (qa_chain) será inicializada de forma "lazy" (preguiçosa) na primeira requisição.
qa_chain = None

async def _initialize_async():
    """
    Função assíncrona que contém a lógica de inicialização real.
    Esta função é chamada apenas uma vez por worker para configurar o estado.
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

    # --- INICIALIZAÇÃO DOS COMPONENTES LANGCHAIN ---
    print("DEBUG: Criando GoogleGenerativeAIEmbeddings...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    print("DEBUG: GoogleGenerativeAIEmbeddings criado com sucesso.")

    print("DEBUG: Criando Chroma vector store...")
    vector_store = Chroma(persist_directory=CHROMA_LOCAL_DIR, embedding_function=embeddings)
    print("DEBUG: Chroma vector store criado com sucesso.")

    print("DEBUG: Criando ChatGoogleGenerativeAI...")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
    print("DEBUG: ChatGoogleGenerativeAI criado com sucesso.")

    # --- DEFINIÇÃO DO PROMPT ---
    prompt_template = """
Contexto:
{context}

Faça um levantamento sobre o item "{question}" e busque informações complementares sobre ele, como NCM e descrição completa.
Após isso, compare detalhadamente os dados levantados com o contexto fornecido acima e verifique tratamentos tributários diferenciados, peculiaridades, alíquotas, etc.

Utilize a versão do contexto como fonte mais correta. Toda a base legal deve ser extraída do contexto.

Após a análise, forneça um resumo detalhado e claro do tratamento tributário para o item.

O resumo deve obrigatoriamente incluir os seguintes pontos, quando aplicáveis:

1.  **Alíquota Interna:** Qual a alíquota padrão de ICMS para este produto em operações dentro de SC?
2.  **Substituição Tributária (ICMS-ST):** O produto está sujeito ao regime de ST? Se sim, mencione o MVA/IVA-ST aplicável (original e ajustado para 4% e 12%, se houver) e a base legal (dispositivo do RICMS/SC).
3.  **Isenção:** Existe alguma isenção de ICMS para este produto? Se sim, qual e sob quais condições? Citar a base legal.
4.  **Redução de Base de Cálculo:** Há alguma redução na base de cálculo do ICMS? Se sim, qual o percentual e as condições? Citar a base legal.
5.  **Crédito Presumido:** Existe algum benefício de crédito presumido? Se sim, qual o percentual e para qual tipo de empresa/operação se aplica? Citar a base legal.
6.  **Observações Importantes:** Qualquer outra informação relevante, como regimes especiais, diferimento, ou particularidades da operação.

Formate a resposta usando Markdown, com títulos claros para cada seção (ex: ## Alíquota, ## Substituição Tributária).
Caso alguma informação não possa ser encontrada no contexto, pode ser buscada fora dele, porém essas informações devem ser destacadas com o texto "obtida fora da Base de Dados".
O sistema está livre para fazer inferências e conjecturas utilizando as informações obtidas.
Aja como um consultor tributário especialista em legislação catarinense.
"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # CORREÇÃO 2 (PRINCIPAL): A criação do `qa_chain` foi movida para dentro desta função.
    # Isso garante que `llm` e `vector_store` já existam antes de serem usados.
    # Este era o motivo do erro de inicialização do contêiner.
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 40, "fetch_k": 50}
        ),
        chain_type_kwargs={"prompt": PROMPT}
    )

    print("INFO: Inicialização do worker concluída com sucesso.")

def initialize_worker_state():
    """
    Invólucro síncrono para executar a inicialização assíncrona.
    """
    global qa_chain
    if qa_chain is not None:
        return # Evita reinicialização desnecessária

    try:
        print("INFO: Iniciando estado para um novo worker (lazy initialization)...")
        asyncio.run(_initialize_async())
    except Exception as e:
        print(f"ERRO FATAL durante a inicialização do worker: {e}", file=sys.stderr)
        # Mantém qa_chain como None para que futuras requisições saibam que a inicialização falhou.
        qa_chain = None

@functions_framework.http
def executar_consulta(request):
    """
    Ponto de entrada da Cloud Function HTTP.
    """
    global qa_chain
    
    # Configuração dos headers para permitir CORS (Cross-Origin Resource Sharing)
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    # Responde a requisições pre-flight do tipo OPTIONS
    if request.method == 'OPTIONS':
        return ('', 204, headers)

    try:
        # Inicializa o estado do worker na primeira requisição, se ainda não foi feito.
        if qa_chain is None:
            initialize_worker_state()
        
        # Se a inicialização falhou, retorna um erro de serviço indisponível.
        if qa_chain is None:
            raise RuntimeError("O serviço não está disponível devido a um erro de inicialização do worker.")

        request_json = request.get_json(force=True)
        query = request_json.get("query")
        if not query:
            raise ValueError("O campo 'query' é obrigatório no corpo do JSON.")

        # Utiliza o loop de eventos existente para executar a função assíncrona da cadeia de QA
        resultado_dict = asyncio.run(qa_chain.ainvoke({"query": query}))
        resultado = resultado_dict.get("result", "Não foi possível obter uma resposta.")
        
        return ({"resposta": resultado}, 200, headers)

    except ValueError as e:
        return ({"error": f"Requisição inválida: {e}"}, 400, headers)
    except Exception as e:
        print(f"Erro interno ao processar a consulta: {e}", file=sys.stderr)
        return ({"error": "Ocorreu um erro interno ao processar sua solicitação."}, 500, headers)
