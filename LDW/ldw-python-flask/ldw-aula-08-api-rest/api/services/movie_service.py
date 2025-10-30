from api import mongo
from ..models import movie_model

def add_movie(movie):
    mongo.db.movies.insert_one(
        {
            'title': movie.title,
            'description':movie.description,
            'year':movie.year,
            'duration': movie.duration
        }
    )
    
# Função para listar
def get_movies(movie):
    return list(mongo.db.movies.find())