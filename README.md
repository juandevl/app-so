A continuación, el gráfico muestra como la aplicación gestiona las solicitudes HTTP enviadas por el usuario.

[ Usuario ]

     │ Solicitud HTTP
     ▼
[ Apache HTTP Server ] 

     │ WSGI (redirecciona)
     ▼
[ App Flask (Python) ] 

     │ CRUD (pymongo)
     ▼
[ BDD (MongoDB) ]

     │ json response
     ▼
[ App Flask (Python) ]

     │
     ▼
[ Apache HTTP Server ]

     │
     ▼
[ Usuario ]


+------------------------------+
|        Docker Compose        |
|   +-----------------------+  |
|   | Contenedor BDD MongoDB|  |
|   |       	            |  |
|   +-----------------------+  |
|              ▲               |
|              │ PYMONGO       |
|              ▼               |
|   +-----------------------+  |
|   | Contenedor Flask      |  |
|   | Apache Python         |  |
|   |                       |  |
|   +-----------------------+  |
+------------------------------+

[ Usuario ]                               +------------------------------+
     │ Solicitud HTTP                     |        Docker Compose        |
     ▼                                    |   +-----------------------+  |
[ Apache HTTP Server ]                    |   | Contenedor BDD MongoDB|  |
     │ WSGI (redirecciona)                |   |       			      |  |
     ▼                                    |   +-----------------------+  |
[ App Flask (Python) ]                    |              ▲               |
     │ CRUD (pymongo)                     |              │ PYMONGO       |
     ▼                                    |              ▼               |
[ BDD (MongoDB) ]                         |   +-----------------------+  |
     │ json response                      |   | Contenedor Flask      |  |
     ▼                                    |   | Apache Python         |  |
[ App Flask (Python) ]                    |   |        PTO80          |  |
     │                                    |   +-----------------------+  |
     ▼                                    +------------------------------+
[ Apache HTTP Server ]                   
     │
     ▼
[ Usuario ]



# Aplicación Web CRUD - Gestión de Juegos de Mesa

Este proyecto consiste en una aplicación web CRUD que permite a los usuarios:

- Insertar juegos de mesa.
- Actualizar juegos de mesa.
- Eliminar juegos de mesa.
- Mostrar todos los juegos almacenados en la base de datos.

La aplicación está respaldada por una infraestructura basada en **contenedores Docker**, lo que facilita su ejecución y despliegue. El sistema se divide en dos contenedores:

- **Contenedor Flask + Apache + WSGI: Este contenedor maneja la lógica de la aplicación web, las interacciones con el usuario, y la ejecución de Python y JavaScript.**
- **Contenedor MongoDB: Este contenedor es responsable del almacenamiento y gestión de datos, usando MongoDB como base de datos.**

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```bash
/flask-app
  ├── src/                          # Código de la aplicación
  │    ├── static/
  │    │     ├── css/
  │    │     │    ├── main.css
  │    │     ├── js/
  │    │          ├── script.js
  │    ├── templates/
  │          ├── games.html
  │          ├── home.html
  │          ├── layout.html
  │          ├── new_game.html
  │          ├── update.html
  │    ├── __init__.py
  │    ├── routes.py                # Rutas de la aplicación
  │    └── ... (otros archivos)
  ├── Dockerfile                    # Archivo para construir la imagen Docker
  ├── docker-compose.yml            # Configuración para Docker Compose
  ├── requirements.txt              # Dependencias de Python
  ├── apache-config.conf            # Configuración personalizada de Apache
  ├── app.wsgi                      # Archivo para gestionar la comunicacion entre Flask y Apache
  ├── .dockerignore                 # Archivos que no deben ser incluidos en la imagen
  └── README.md                     # Este archivo
```

## Requisitos
Para ejecutar esta aplicación en tu máquina, necesitas tener instalados los siguientes requisitos:

- **Docker** (y Docker Compose): Asegúrate de tener Docker y Docker Compose instalados. Si no los tienes, puedes descargarlos desde docker.com.
- **Git** (opcional, para clonar el repositorio)
Instalación
1. Clonar el repositorio
Si aún no has clonado el repositorio, puedes hacerlo usando Git:

git clone https://github.com/tu_usuario/mi-aplicacion-crud.git
cd mi-aplicacion-crud
2. Construir y ejecutar los contenedores con Docker Compose
Usamos Docker Compose para facilitar la configuración y ejecución de ambos contenedores (uno para la aplicación y otro para MongoDB).

Primero, asegúrate de que estás en la raíz del proyecto (donde está ubicado el archivo docker-compose.yml).

docker-compose up --build
Este comando realiza lo siguiente:

Construye las imágenes Docker a partir del Dockerfile y las configuraciones proporcionadas.
Levanta dos contenedores:
Contenedor Flask + Apache + WSGI: Servirá la aplicación web.
Contenedor MongoDB: Proporciona la base de datos.
Docker Compose se encargará de gestionar la comunicación entre ambos contenedores.

3. Acceder a la aplicación web
Una vez que los contenedores estén en funcionamiento, puedes acceder a la aplicación web desde tu navegador web. Abre la siguiente URL:

http://localhost:80
4. Detener los contenedores
Si deseas detener los contenedores y limpiar el entorno, puedes hacerlo con el siguiente comando:

bash
Copiar código
docker-compose down
Este comando detendrá los contenedores y eliminará los recursos asociados.

Estructura de la Aplicación
1. Contenedor Flask + Apache + WSGI
Flask: El framework web en Python que gestiona las rutas y lógica de la aplicación.
Apache HTTP Server: Servidor web que gestiona las solicitudes HTTP y las redirige a la aplicación Flask a través de mod_wsgi.
mod_wsgi: Módulo de Apache que permite ejecutar aplicaciones Python dentro de Apache.
2. Contenedor MongoDB
MongoDB es la base de datos NoSQL utilizada para almacenar los juegos de mesa. Los contenedores se comunican a través de la red interna de Docker, y Flask interactúa con MongoDB utilizando la biblioteca pymongo para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

3. Archivos Importantes
Dockerfile: Define cómo construir la imagen de Docker para la aplicación Flask con Apache.
docker-compose.yml: Configura y orquesta los contenedores de Docker para la aplicación y MongoDB.
requirements.txt: Contiene las dependencias de Python necesarias para ejecutar la aplicación Flask (Flask, pymongo, etc.).
apache-config.conf: Configuración personalizada para Apache, que incluye el manejo de solicitudes HTTP y la configuración de mod_wsgi.
.dockerignore: Archivos y directorios que Docker ignorará al construir la imagen (por ejemplo, archivos temporales o entornos virtuales).
Funcionalidad de la Aplicación
La aplicación permite gestionar un conjunto de juegos de mesa a través de un API RESTful con las siguientes rutas (por ejemplo):

GET /juegos: Obtiene todos los juegos de mesa almacenados.
POST /juegos: Inserta un nuevo juego de mesa en la base de datos.
PUT /juegos/{id}: Actualiza la información de un juego de mesa.
DELETE /juegos/{id}: Elimina un juego de mesa de la base de datos.
Contribuciones
Si deseas contribuir a este proyecto, puedes seguir los siguientes pasos:

Haz un fork del repositorio.
Crea una rama nueva para tu funcionalidad o corrección.
Realiza tus cambios y haz un commit.
Push a tu rama y abre un pull request con una descripción detallada de los cambios.
Licencia
Este proyecto está bajo la licencia MIT.

Notas adicionales:
Si tienes algún problema al ejecutar los contenedores o la aplicación, asegúrate de que Docker está correctamente instalado y configurado en tu máquina.
Si deseas más información sobre cómo personalizar la aplicación o los contenedores, revisa los archivos Dockerfile, docker-compose.yml, y apache-config.conf.