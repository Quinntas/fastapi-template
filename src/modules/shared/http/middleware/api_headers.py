from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp


class ApiHeaders(BaseHTTPMiddleware):
    """
    Middleware class to add custom headers to API responses.

    Args:
        app (ASGIApp): The ASGI application.

    Attributes:
        app (ASGIApp): The ASGI application.

    Example:
        ```python
        app = FastAPI()

        app.add_middleware(ApiHeaders)

        @app.get("/")
        async def root():
            return {"message": "Hello, World!"}
        ```
    """

    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers.append("server", "FastAPI")
        response.headers.append("x-powered-by", "FastAPI")
        return response
