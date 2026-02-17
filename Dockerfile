FROM python:3.11-slim
#Esto utiliza la version de python liviana
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONBUFFERED=1
#Estas variables sirven para que 1. No me muestre por consola que tengo que upogretear pip y 2. Para que no haya retraso en los logs

WORKDIR /App
#Donde va a estar mi directorio, si no existe lo crea

COPY requirements.txt .
#Copia el archivo requirementes y lo pega en mi workdir

RUN python -m venv venv
#Creo un entorno virtual

RUN /bin/bash -c "source venv/bin/activate"
#Ejecuto el entorno virtual

RUN pip install -r requirements.txt
#Instalo todas las librerias necesarias

COPY . .
#Copio el resto de los archivos que estan en mi directorio y los copio en el directorio de mi imagen

EXPOSE 8000
#Expongo un puerto

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
#Comando para ejecutar la aplicacion