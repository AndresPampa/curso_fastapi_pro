from pydantic import BaseModel, Field, validator, field_validator
from typing import Optional, List
from datetime import datetime


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