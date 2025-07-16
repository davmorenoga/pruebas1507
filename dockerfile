# Usar una imagen base de Python
FROM python:3.9-slim

# Copiar todos los archivos del proyecto al contenedor
COPY . /app

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar las dependencias necesarias
RUN pip install -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "5000"]
