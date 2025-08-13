# Usa uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o script principal para o diretório de trabalho
COPY main.py .

# Define o comando que será executado quando o contêiner iniciar
CMD ["python", "main.py"]
