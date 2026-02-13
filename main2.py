#OAUTH2
from fastapi import FastAPI, Form, Depends
import fastapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import  Annotated
from fastapi.exceptions import HTTPException
from jose import jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

users = {
    'pablo': {'username': 'pablo', 'email': 'pablo@mail.com', 'password': 'fakepass'},
    'user2': {'username': 'user2', 'email': 'user2@mail.com', 'password': 'user2'},
}

def encode_token(payload: dict) ->str:
    token = jwt.encode(payload, "my-secret", algorithm="HS256")#guardar la clave en variables de entorno
    return token

def decode_token(token:Annotated[str, Depends(oauth2_scheme)]) -> dict:
    data = jwt.decode(token, "my-secret", algorithms=["HS256"])
    user = users.get(data['username'])
    return user


@app.post("/token")
def login(from_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(from_data.username)
    if not user or from_data.password != user['password']:
        raise HTTPException(status_code=400, detail='Incorrect User or Password')
    
    token = encode_token({'username': user['username'], 'email':user['email']})

    return {'access_token': token}

#Ruta protegida por el token
@app.get('/users/profile')
def profile(my_user: Annotated[dict, Depends(decode_token)]): #Annotated[dict, Depends(decode_token)] <-- protege la ruta
    return my_user