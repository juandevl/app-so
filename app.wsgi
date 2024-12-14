import sys
import os

# Especifica la ruta de tu entorno virtual
venv_path = '/app/venv'  # Ruta al entorno virtual dentro del contenedor
sys.path.insert(0, os.path.join(venv_path, 'lib', 'python3.12', 'site-packages'))  # Ajusta la versión de Python según sea necesario

# Agregamos la carpeta 'src' al path para que podamos importar la app de allí
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Importamos la aplicación Flask desde el paquete 'src'
from src import app as application
