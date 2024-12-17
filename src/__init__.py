from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config['MONGO_URI']='mongodb://localhost:27017/gamesdb'    # Descomentar para utilizar localmente con contenedor de MongoDB 
app.config['MONGO_URI']='mongodb://mongo-gamesdb:27017/gamesdb'  #Direccion de conexion entre contenedores con contenedor con MongoDB
mongo = PyMongo(app)

from src import routes

    
