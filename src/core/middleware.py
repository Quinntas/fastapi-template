from typing import List, Type

from fastapi.routing import APIRoute
from starlette.middleware import Middleware
from starlette.types import ASGIApp


def middleware_wrapper(middleware_classes: List[Type[ASGIApp]]):
    """
    Wrapper function that takes a list of middleware classes and returns a custom APIRoute class.

    :param middleware_classes: A list of ASGIApp classes representing the middleware to be applied.
    :return: A custom APIRoute class with the middleware applied.
    """

    class CustomAPIRoute(APIRoute):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            app = self.app
            middlewares = [Middleware(cls) for cls in middleware_classes]
            for middleware in reversed(middlewares):
                app = middleware.cls(app=app)
            self.app = app

    return CustomAPIRoute
