from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI()

# app.title = "Mi primera app con FastAPI"
# app.version =  "2.0.0"

#clase de pydantic
class Movie(BaseModel):
    id:int
    title:str
    overview:str
    year:int
    rating:float
    category:str

class MovieUpdate(BaseModel):
    title:str
    overview:str
    year:int
    rating:float
    category:str

class MovieCreate(BaseModel):
    id:int
    title:str = Field(min_length=5, max_length=30)#, default="My Movie")
    overview:str = Field(min_length=15, max_length=50)#, default="Esta peli trata acerca de...")
    year:int = Field(le=datetime.now().year, ge=1900)#, default=2025)
    rating:float = Field(ge=0, le=10)#, default=5.0)
    category:str = Field(min_length=5, max_length=30)#, default="Accion")
    #gt = greater than
    #ge = greater than or equal
    #lt = less than
    #le = less than or equal
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title': 'mi pelicula',
                'overview': 'Esta peli trata sobre...',
                'year': 2025,
                'rating': 4.6,
                'category': 'porno estar'
            }
        }
    }

movies: List[Movie] = []

# movies = [
#     {
#         "id": 1,
#         "title": "Avatar",
#         "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         "year": "2009",
#         "rating": 7.8,
#         "category": "Acción"
#     },

#     {
#         "id": 2,
#         "title": "Avatar 2",
#         "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         "year": "2029",
#         "rating": 8.8,
#         "category": "Acción"
#     }

# ]


@app.get('/', tags=['Home'])
def home() -> str:
    return "hello World!"

@app.get('/movies', tags=['Movies'])
def get_movies() -> List[Movie]:
    # return {"hello": "world"}
    # return HTMLResponse('<h1>Hello World! MADAFAKA!</h1>')
    return movies


#parametros de ruta
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id:int) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return movie.model_dump()
    
    return []


#localhost:5000/movies/?category=Accion&year=2020
#localhost:5000/movies/?id=123
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category:str, year:int) -> Movie:
    for movie in movies:
        if movie['category'] == category:
            return movie.model_dump()


#Metodo POST
@app.post('/movies', tags=['Movies'])
def create_movies(movie: MovieCreate) -> List[Movie]:

    movies.append(movie)

    return [movie.model_dump() for movie in movies]


@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id:int, movie:MovieUpdate) -> List[Movie]:
    
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category

            return [movie.model_dump() for movie in movies]


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id:int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
        
            return [movie.model_dump() for movie in movies]