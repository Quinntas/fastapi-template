import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    """
    Middleware class for measuring the processing time of a request.

    Args:
        app (ASGIApp): The ASGI application to be wrapped with the middleware.

    Attributes:
        app (ASGIApp): The ASGI application being wrapped.

    """

    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["x-process-time"] = str(process_time)
        return response
