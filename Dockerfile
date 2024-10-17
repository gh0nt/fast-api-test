# Usamos la imagen base de Python 3.12-slim
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app


# Instalamos las dependencias necesarias
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copiamos todo el código de la aplicación al contenedor
COPY . .

# Exponemos el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para correr la aplicación con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
