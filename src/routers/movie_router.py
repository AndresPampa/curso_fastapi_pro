from fastapi import FastAPI, Body, Path, Query, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from src.models.movie_models import Movie, MovieUpdate, MovieCreate
from typing import List

movies: List[Movie] = []

movie_rounter = APIRouter()

@movie_rounter.get('/', tags=['Movies'])#, status_code=500, response_description='Esta bien rey') #, status_code=200 # -> para documentacion
def get_movies() -> List[Movie]:
    content =  [movie.model_dump() for movie in movies] #DESCOMENTAR!
    return JSONResponse(content=content, status_code=200)

#parametros de ruta
@movie_rounter.get('/{id}', tags=['Movies'])
def get_movie(id:int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump(), status_code=200)
    
    return JSONResponse(content={}, status_code=404)


#localhost:5000/movies/?category=Accion&year=2020
#localhost:5000/movies/?id=123
@movie_rounter.get('/by_category', tags=['Movies'])
def get_movie_by_category(year:int, category:str = Query(min_length=5, max_length=20)) -> Movie | dict:
    for movie in movies:
        if movie.category == category:
            return JSONResponse(content=movie.model_dump(), status_code=200)
        
    return JSONResponse(content={}, status_code=404)

#Metodo POST
@movie_rounter.post('/', tags=['Movies'])
def create_movies(movie: MovieCreate) -> JSONResponse:
    movies.append(movie)

    content =  [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=201)
    # return RedirectResponse(url='/movies', status_code=303)


@movie_rounter.put('/{id}', tags=['Movies'])
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


@movie_rounter.delete('/{id}', tags=['Movies'])
def delete_movie(id:int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
        
            return JSONResponse(content=[movie.model_dump() for movie in movies], status_code=200)


# @movie_rounter.get('/get_file/', tags=['files'])
# def get_file() -> FileResponse:
#     return FileResponse('file.pdf', status_code=200)