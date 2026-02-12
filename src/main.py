from fastapi import FastAPI, Body, Path, Query, status
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse, Response
from src.routers.movie_router import movie_rounter
from src.utils.http_error_handler import HTTPErrorHandler
from fastapi.requests import Request

app = FastAPI()

# app.title = "Mi primera app con FastAPI"
# app.version =  "2.0.0"

# app.add_middleware(HTTPErrorHandler)
@app.middleware(middleware_type='http')
async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
    try:
        print("Middleware is RUN Bith!")
        return await call_next(request)
    except Exception as e:
        content_error = f"exc: {str(e)}"
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=content_error, status_code=status_code)



@app.get('/', tags=['Home'])
def home() -> str:
    return PlainTextResponse(content='HOME', status_code=200)


app.include_router(prefix ='/movies', router=movie_rounter)
