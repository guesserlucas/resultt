import os
import shutil
import functions_framework
from google.cloud import storage
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- CONFIGURAÇÃO ---
BUCKET_NAME = os.environ.get("BUCKET_NAME")
CHROMA_BUCKET_PATH = "chroma_db_ricms"
CHROMA_LOCAL_DIR = "/tmp/chroma_db"

# --- PONTO DE ENTRADA (ENTRY POINT) ---
@functions_framework.http
async def executar_consulta(request):
    # Configura CORS para permitir requisições de qualquer origem
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    # Trata requisições OPTIONS (preflight CORS)
    if request.method == 'OPTIONS':
        return ('', 204, headers)

    # Inicia um único bloco try para toda a lógica de processamento
    try:
        # 1. Análise e validação da requisição JSON
        request_json = request.get_json(force=True)
        if request_json is None:
            raise ValueError("Corpo da requisição JSON não pode ser nulo.")
        
        query = request_json.get("query")
        if not query:
            raise ValueError("O campo 'query' é obrigatório no corpo do JSON.")

        # 2. Lógica de negócio principal
        storage_client = storage.Client()
        
        if os.path.exists(CHROMA_LOCAL_DIR):
            shutil.rmtree(CHROMA_LOCAL_DIR)
        os.makedirs(CHROMA_LOCAL_DIR, exist_ok=True)

        # Baixa o banco de dados Chroma do GCS
        bucket = storage_client.bucket(BUCKET_NAME)
        blobs = storage_client.list_blobs(BUCKET_NAME, prefix=CHROMA_BUCKET_PATH)
        
        downloaded_files = 0
        for blob in blobs:
            if not blob.name.endswith('/'):
                destination_file_name = os.path.join(CHROMA_LOCAL_DIR, os.path.relpath(blob.name, CHROMA_BUCKET_PATH))
                os.makedirs(os.path.dirname(destination_file_name), exist_ok=True)
                blob.download_to_filename(destination_file_name)
                downloaded_files += 1
        
        if downloaded_files == 0:
            raise FileNotFoundError(f"Nenhum arquivo de banco de dados vetorial encontrado em gs://{BUCKET_NAME}/{CHROMA_BUCKET_PATH}.")

        # Inicializa os componentes do LangChain
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

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
            chain_type_kwargs={"prompt": PROMPT}
        )

        # 3. Executa a cadeia de forma assíncrona
        resultado_dict = await qa_chain.ainvoke({"query": query})
        resultado = resultado_dict.get("result", "Não foi possível obter uma resposta.")
        
        return ({"resposta": resultado}, 200, headers)

    except ValueError as e:
        print(f"Erro na validação da requisição: {e}")
        return ({"error": f"Requisição inválida: {e}"}, 400, headers)
    except FileNotFoundError as e:
        print(f"Erro de configuração do servidor: {e}")
        return ({"error": f"Erro de configuração interna: {e}"}, 500, headers)
    except Exception as e:
        print(f"Erro interno ao processar a consulta: {e}")
        return ({"error": "Ocorreu um erro interno ao processar sua solicitação."}, 500, headers)
