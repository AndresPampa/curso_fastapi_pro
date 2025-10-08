from fastapi import FastAPI


app = FastAPI()

# app.title = "Mi primera app con FastAPI"
# app.version =  "2.0.0"

@app.get('/', tags=['Home'])
def home() -> str:
    return "hello World!"
