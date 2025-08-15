# backend-consulta-ricms/api-service/main_corrigido.py

import os
import shutil
import asyncio  # PASSO 3: Importar a biblioteca asyncio
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
# PASSO 1: A função principal deve ser síncrona (def) e não assíncrona (async def)
def executar_consulta(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    if request.method == 'OPTIONS':
        return ('', 204, headers)

    try:
        request_json = request.get_json(force=True)
        if request_json is None:
            raise ValueError("Corpo da requisição JSON não pode ser nulo.")
        
        query = request_json.get("query")
        if not query:
            raise ValueError("O campo 'query' é obrigatório no corpo do JSON.")

        storage_client = storage.Client()
        
        if os.path.exists(CHROMA_LOCAL_DIR):
            shutil.rmtree(CHROMA_LOCAL_DIR)
        os.makedirs(CHROMA_LOCAL_DIR, exist_ok=True)

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

        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = Chroma(persist_directory=CHROMA_LOCAL_DIR, embedding_function=embeddings)

        # PASSO 2: Encapsular a lógica assíncrona em uma função interna `async def`
        async def _get_qa_response_async(user_query, db):
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
                retriever=db.as_retriever(search_kwargs={"k": 5}),
                chain_type_kwargs={"prompt": PROMPT}
            )
            # A chamada assíncrona real acontece aqui dentro
            resultado_dict = await qa_chain.ainvoke({"query": user_query})
            return resultado_dict.get("result", "Não foi possível obter uma resposta.")

        # PASSO 3: Chamar a função assíncrona a partir do contexto síncrono usando asyncio.run()
        resultado = asyncio.run(_get_qa_response_async(query, vector_store))
        
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
