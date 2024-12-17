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

### Pasos para la instalacion

1. Ubicarse en el directorio raíz del proyecto (donde se encuentran los archivos Dockerfile y docker-compose.yml)
2. Abrir una terminal y ejecutar los siguientes comandos:
