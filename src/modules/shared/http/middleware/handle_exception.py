import traceback

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.errors import HttpException
from src.core.responses import json_response


async def handle_exception(request: Request, exc: Exception) -> Response:
    """
    Handle an exception in a web request.

    :param request: The incoming web request that caused the exception.
    :param exc: The exception that was raised.
    :return: A web response indicating the result of handling the exception.
    :rtype: Response
    """
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
    """
    This class handles exceptions that occur during the execution of a request in a web application.

    Class: HandleException

    Inherits from: BaseHTTPMiddleware

    Methods:
        - dispatch: Handles the request and calls the next middleware or application. If an exception occurs during the execution of the request, it calls the 'handle_exception' function to handle the exception.

    Usage example:

    ```
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.requests import Request

    class MyExceptionMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request: Request, call_next):
            try:
                return await call_next(request)
            except Exception as e:
                return await handle_exception(request, e)
    ```
    """

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            return await handle_exception(request, e)
