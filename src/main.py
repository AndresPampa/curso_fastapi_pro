from sys import int_info
from fastapi import FastAPI, Body, Path, Query, status
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse, Response
from src.routers.movie_router import movie_rounter
from src.utils.http_error_handler import HTTPErrorHandler
from fastapi.requests import Request
#Jinja
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

#Depends
from fastapi import Depends
from typing import Annotated


def dependency1(param1:int):
    print("Gobal dependency 1")

def dependency2(param2: int):
    print("Gobal dependency 2")

#Declarar dependencias de forma global
app = FastAPI(dependencies=[Depends(dependency1), Depends(dependency2)])

# app.title = "Mi primera app con FastAPI"
# app.version =  "2.0.0"

app.add_middleware(HTTPErrorHandler)
# @app.middleware(middleware_type='http')
# async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
#     try:
#         print("Middleware is RUN Bith!")
#         return await call_next(request)
#     except Exception as e:
#         content_error = f"exc: {str(e)}"
#         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#         return JSONResponse(content=content_error, status_code=status_code)

#Definimos los directorios donde van a estar los archivos staticos y los templates
static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')

app.mount(path='/static', app=StaticFiles(directory=static_path), name='static')
templates = Jinja2Templates(directory=templates_path)


@app.get('/', tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request,'message': 'welcome'})

#Injeccion de dependencias
# FUNCION
# def common_params(start_date:str, end_date:str):
#     return {'start_date': start_date, 'end_date': end_date}

# CommonDep = Annotated[dict, Depends(common_params)]

#CLASE
class CommonDep:
    def __init__(self, start_date:str, end_date:str) -> None:
        self.start_date = start_date
        self.end_date = end_date





@app.get('/users')
def get_users(commons: CommonDep = Depends()): #country:str = Annotated[str, Query(max_length=10)]
    return f"Users created between {commons.start_date} and {commons.end_date}"


@app.get('/customers')
def get_customers(commons: CommonDep = Depends()): #En depends no le pasamos ningun parametro porque ya dijimos que es te tipo CommonDep
    return f"customers created between {commons.start_date} and {commons.end_date}"


app.include_router(prefix ='/movies', router=movie_rounter)
