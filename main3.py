from fastapi import FastAPI, HTTPException, Header, Request, Response, Depends
from typing import Annotated

app = FastAPI()

def get_headers(access_token:Annotated[str | None, Header(max_length= 100)]= None,
                user_role:Annotated[str | None, Header()]= None):

    if access_token != 'secret_token':
        raise HTTPException(status_code=401, detail="No pasas por gato")
    return {'access_token': access_token, 'user_role':user_role}



@app.get('/dashboard')
def dashboard(headers: Annotated[dict, Depends(get_headers)],
            request:Request,
            response:Response):

    print(request.headers)
    response.headers["user_status"] = "ENABLED"

    return {"access_token":headers['access_token'], "user_role":headers['user_role']}
    
