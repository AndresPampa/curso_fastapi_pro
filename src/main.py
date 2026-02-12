from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime
from src.models.movie_models import Movie, MovieUpdate, MovieCreate
from src.routers.movie_router import movie_rounter

app = FastAPI()

# app.title = "Mi primera app con FastAPI"
# app.version =  "2.0.0"

@app.get('/', tags=['Home'])
def home() -> str:
    return PlainTextResponse(content='HOME', status_code=200)


app.include_router(prefix ='/movies', router=movie_rounter)
