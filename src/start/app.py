from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from src.core.exception import HttpException
from src.start.routes import v1_router

app = FastAPI()


@app.exception_handler(HttpException)
async def http_exception_handler(request: Request, exc: HttpException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_dict()
    )


app.include_router(v1_router)
