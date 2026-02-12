from fastapi import FastAPI, status
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.responses import JSONResponse

class HTTPErrorHandler(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)


    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        #que hace el call_next? ==> cuando queremos acceder a una ruta se ejecuta primero el middelware ahi le podes
        #agregar una logica y despues llama a la siguiente funcion o call_next
        try:
            return await call_next(request)
        except Exception as e:
            content_error = f"exc: {str(e)}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content=content_error, status_code=status_code)