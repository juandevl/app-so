# Usamos una imagen base de Python
FROM python:3.12-slim

# Instalamos Apache, mod_wsgi y dependencias necesarias
RUN apt-get update && \
    apt-get install -y apache2 apache2-dev && \
    apt-get install -y libapache2-mod-wsgi-py3 && \
    apt-get clean

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requerimientos y las dependencias de Python
COPY requirements.txt /app/requirements.txt

# Creamos y activamos el entorno virtual
RUN python3 -m venv /app/venv  # Crea el entorno virtual en /app/venv
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt  # Instala las dependencias en el entorno virtual

# Copiamos el código de la aplicación al contenedor
COPY . /app

# Activamos el módulo de WSGI de Apache
RUN a2enmod wsgi

# Copiamos la configuración de Apache
COPY apache-flask.conf /etc/apache2/sites-available/000-default.conf

# Exponemos el puerto 80 para que Apache pueda manejar las solicitudes
EXPOSE 80

# Iniciamos Apache en el contenedor
CMD ["apache2ctl", "-D", "FOREGROUND"]

