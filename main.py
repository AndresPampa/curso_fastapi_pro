from fastapi import FastAPI
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
    }
]



@app.get('/', tags=['Home'])
def home() -> str:
    return "hello World!"

@app.get('/movies', tags=['Home'])
def home() -> HTMLResponse:
    # return {"hello": "world"}
    # return HTMLResponse('<h1>Hello World! MADAFAKA!</h1>')
    return movies