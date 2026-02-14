from typing import Annotated
from fastapi import FastAPI, Response, Cookie
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/')
def root(response: Response):
    response.set_cookie(key='username', value='tuvieja')
    return JSONResponse(content={"msg": "Welcome"}, headers={"set-cookie": "username=tuvieja"})


@app.get('/users')
def users():
    response = JSONResponse(content={"msg": "Welcome"})
    response.set_cookie(key='username', value='tuvieja', expires=10, path='users')
    return response

@app.get('/users/{id}')
def users_b_id(id:str):
    return id

@app.get('/dashboard')
def dashboard(username: Annotated[str, Cookie()]):
    return username