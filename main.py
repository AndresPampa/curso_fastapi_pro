from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field, validator, field_validator
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
    title:str #= Field(min_length=5, max_length=30)#, default="My Movie")
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

    @field_validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError('El titulo es muy corto')

        if len(value) > 15:
            raise ValueError('El titulo es muy largo')
        
        return value



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
    return PlainTextResponse(content='Home', status_code=200)

@app.get('/movies', tags=['Movies'])#, status_code=500, response_description='Esta bien rey') #, status_code=200 # -> para documentacion
def get_movies() -> List[Movie]:
    # return {"hello": "world"}
    # return HTMLResponse('<h1>Hello World! MADAFAKA!</h1>')
    content =  [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)


#parametros de ruta
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id:int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump(), status_code=200)
    
    return JSONResponse(content={}, status_code=404)


#localhost:5000/movies/?category=Accion&year=2020
#localhost:5000/movies/?id=123
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(year:int, category:str = Query(min_length=5, max_length=20)) -> Movie | dict:
    for movie in movies:
        if movie.category == category:
            return JSONResponse(content=movie.model_dump(), status_code=200)
        
    return JSONResponse(content={}, status_code=404)

#Metodo POST
@app.post('/movies', tags=['Movies'])
def create_movies(movie: MovieCreate) -> JSONResponse:
    movies.append(movie)

    content =  [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)
    # return RedirectResponse(url='/movies', status_code=303)


@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id:int, movie:MovieUpdate) -> List[Movie]:
    
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.overview = movie.overview
            item.year = movie.year
            item.rating = movie.rating
            item.category = movie.category

    content =  [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id:int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
        
            return JSONResponse(content=[movie.model_dump() for movie in movies], status_code=200)


# @app.get('/get_file/', tags=['files'])
# def get_file() -> FileResponse:
#     return FileResponse('file.pdf', status_code=200)