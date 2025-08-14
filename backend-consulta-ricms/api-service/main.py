import os
import shutil
import functions_framework
from google.cloud import storage
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

# --- CONFIGURAÇÃO ---
BUCKET_NAME = os.environ.get("BUCKET_NAME")
CHROMA_BUCKET_PATH = "chroma_db_ricms"
CHROMA_LOCAL_DIR = "/tmp/chroma_db"

# --- PONTO DE ENTRADA (ENTRY POINT) ---
@functions_framework.http
def executar_consulta(request):
    # Configura CORS para permitir requisições de qualquer origem
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
            # Esta verificação captura casos onde o corpo é 'null'
            raise ValueError("Corpo da requisição JSON não pode ser nulo.")
        query = request_json.get("query")
        if not query:
            raise ValueError("O campo 'query' é obrigatório no corpo do JSON.")
    except Exception as e:
        # Captura erros de análise do JSON (force=True), ValueErrors, etc.
        print(f"Erro na análise da requisição: {e}")
        return ({"error": f"Requisição inválida: {e}"}, 400, headers)

    # A lógica principal agora pode assumir que 'query' é válido.
    try:
        #... Restante da lógica de negócio...

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        blobs = storage_client.list_blobs(BUCKET_NAME, prefix=CHROMA_BUCKET_PATH)

        if os.path.exists(CHROMA_LOCAL_DIR):
            shutil.rmtree(CHROMA_LOCAL_DIR)
        os.makedirs(CHROMA_LOCAL_DIR, exist_ok=True)

        for blob in blobs:
            destination_file_name = os.path.join(CHROMA_LOCAL_DIR, os.path.relpath(blob.name, CHROMA_BUCKET_PATH))
            os.makedirs(os.path.dirname(destination_file_name), exist_ok=True)
            blob.download_to_filename(destination_file_name)

        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = Chroma(persist_directory=CHROMA_LOCAL_DIR, embedding_function=embeddings)
        llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 5})
        )

        prompt_otimizado = f"""
        Aja como um consultor tributário especialista em legislação de ICMS de Santa Catarina.
        Baseando-se EXCLUSIVAMENTE no contexto fornecido, responda à pergunta do usuário.
        Se a informação não estiver no contexto, informe: "A informação não foi encontrada na legislação consultada."

        Pergunta do usuário: "Qual o tratamento tributário para {query}?"

        Forneça uma resposta estruturada em Markdown, cobrindo:
        - Alíquota Interna
        - Substituição Tributária (ICMS-ST)
        - Isenção
        - Redução de Base de Cálculo
        - Crédito Presumido
        - Observações Importantes
        - Base Legal para cada item.
        """

        resultado = qa_chain.run(prompt_otimizado)
        return ({"resposta": resultado}, 200, headers)

    except Exception as e:
        print(f"Erro ao processar a consulta: {e}")
        return ({"error": "Ocorreu um erro interno ao processar sua solicitação."}, 500, headers)
