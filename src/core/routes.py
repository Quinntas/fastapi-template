from fastapi import APIRouter

from src.core.controller import Controller
from src.core.middleware import Middleware


def route(router: APIRouter, path: str, methods: list[str], controller: Controller,
          middlewares: list[Middleware] = None):
    async def router_func(*args, **kwargs):
        if middlewares is None or len(middlewares) == 0:
            return await controller.handle(*args, **kwargs)
        else:
            async def call_next(index: int):
                if index < len(middlewares):
                    return await middlewares[index].handle(
                        lambda: call_next(index + 1)
                    )
                else:
                    return await controller.handle(*args, **kwargs)

            return await call_next(0)

    router_func.__annotations__ = controller.handle.__annotations__

    return router.api_route(
        path=path,
        name=controller.name,
        status_code=controller.status_code,
        description=controller.description,
        summary=controller.summary,
        deprecated=controller.deprecated,
        tags=controller.tags,
        methods=methods,
    )(router_func)


def get(router: APIRouter, path: str, controller: Controller):
    return route(router, path, ['get'], controller)


def post(router: APIRouter, path: str, controller: Controller):
    return route(router, path, ['post'], controller)
