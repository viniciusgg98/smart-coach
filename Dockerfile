# Usa uma imagem base com Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script Python para dentro do container
COPY avaliacao.py .

# Define o comando que será executado quando o container rodar
CMD ["python", "avaliacao.py"]