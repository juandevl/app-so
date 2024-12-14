from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config['MONGO_URI']='mongodb://localhost:27017/gamesdb'
app.config['MONGO_URI']='mongodb://mongo-gamesdb:27017/gamesdb'
mongo = PyMongo(app)

from src import routes

    
