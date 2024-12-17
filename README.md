A continuación, el gráfico muestra como la aplicación gestiona las solicitudes HTTP enviadas por el usuario.
```
[ Usuario ]                               +-------------------------------+
     │ Solicitud HTTP                     |        Docker Compose         |
     ▼                                    |   +------------------------+  |
[ Apache HTTP Server ]                    |   | Contenedor BDD MongoDB |  |
     │ WSGI (redirecciona)                |   |       			       |  |
     ▼                                    |   +------------------------+  |
[ App Flask (Python) ]                    |              ▲                |
     │ CRUD (pymongo)                     |              │ PYMONGO        |
     ▼                                    |              ▼                |
[ BDD (MongoDB) ]                         |   +------------------------+  |
     │ json response                      |   | Contenedor Flask       |  |
     ▼                                    |   | Apache Python          |  |
[ App Flask (Python) ]                    |   |        PTO80           |  |
     │                                    |   +------------------------+  |
     ▼                                    +-------------------------------+
[ Apache HTTP Server ]                   
     │
     ▼
[ Usuario ]
```

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

### Pasos para la instalacion

1. Ubicarse en el directorio raíz del proyecto (donde se encuentran los archivos Dockerfile y docker-compose.yml)
2. Abrir una terminal y ejecutar el siguiente comando:
```bash
docker-compose up -d --build
```

Dicho comando realiza el proceso de construcción de los contenedores.
Al finalizar la construcción, quedan en ejecución en segundo plano, liberando el uso de la terminal.

3. Una vez finalizada la construcción de los contenedores y la ejecución de los mismos, debemos dirigirnos hacia nuestro navegador e ingresar la siguiente URL:
**http://localhost:80/**

En dicha URL, se encuentra la aplicación Flask en ejecución, con la base de datos de la aplicacion en MongoDB.

4. Si queremos ver los contenedores funcionando podemos ejecutar el siguiente comando:
```bash
docker ps
```
Dicho comando nos muestra los contenedores en ejecución.

5. Para detener los contenedores, podemos ejecutar los siguientes comandos:
```bash
# Para detener la ejecución y remover los contenedores
docker-compose down

# Para detener la ejecución de los contenedores
docker stop <ID contenedor o NAME>
```

**NOTA:** Si se desea ejecutar nuevamente los contenedores, volver al punto 1.
