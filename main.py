from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse



app = FastAPI()

# app.title = "Mi primera app con FastAPI"
# app.version =  "2.0.0"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },

    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2029",
        "rating": 8.8,
        "category": "Acción"
    }

]


@app.get('/', tags=['Home'])
def home() -> str:
    return "hello World!"

@app.get('/movies', tags=['Movies'])
def get_movies() -> HTMLResponse:
    # return {"hello": "world"}
    # return HTMLResponse('<h1>Hello World! MADAFAKA!</h1>')
    return movies


#parametros de ruta
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id:int) -> HTMLResponse:
    for movie in movies:
        if movie['id'] == id:
            return movie
    
    return []


#localhost:5000/movies/?category=Accion&year=2020
#localhost:5000/movies/?id=123
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category:str, year:int) -> HTMLResponse:
    for movie in movies:
        if movie['category'] == category:
            return movie


#Metodo POST
@app.post('/movies', tags=['Movies'])
def create_movies(id:int=Body(), 
                  title:str=Body(), 
                  overview:str=Body(), 
                  year:int=Body(), 
                  rating:float=Body(), 
                  category:str=Body()) -> HTMLResponse:

    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })

    return movies


@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id:int,
                 title:str=Body(), 
                 overview:str=Body(), 
                 year:int=Body(), 
                 rating:float=Body(), 
                 category:str=Body()) -> HTMLResponse:
    
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category

            return movies


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id:int) -> HTMLResponse:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
        
            return movies