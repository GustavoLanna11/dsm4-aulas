# Importando o Flask no pacote API  
from flask import Flask

# Importando o Flask-restful
from flask_restful import Api

# Importando Pymongo
from flask_pymongo import PyMongo

# Importando marshmallow
from flask_marshmallow import Marshmallow

# Carregando o Flask na variável App
app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/api-movies'


# Carregando o pacote Api do Flask Restful na variável api
api = Api(app)

mongo = PyMongo(app)
ma = Marshmallow(app)
from .resources import movie_resources