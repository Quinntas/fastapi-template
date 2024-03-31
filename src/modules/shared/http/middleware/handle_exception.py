import traceback

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.errors import HttpException
from src.core.responses import json_response


async def handle_exception(request: Request, exc: Exception) -> Response:
    if isinstance(exc, HttpException):
        return json_response(exc.status_code, {
            "message": exc.message,
            **exc.body
        })

    traceback.print_exc()

    return json_response(500, {
        "message": "Internal server error"
    })


class HandleException(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            return await handle_exception(request, e)
