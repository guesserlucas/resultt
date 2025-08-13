# Usa uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt.

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o script principal para o diretório de trabalho
COPY main.py.

# Expõe a porta que o Google Cloud Run usa por padrão
EXPOSE 8080

# Define o comando que será executado quando o contêiner iniciar
CMD ["functions-framework", "--target=executar_consulta", "--port=8080"]
