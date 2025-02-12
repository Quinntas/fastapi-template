from functools import update_wrapper
from inspect import signature
from typing import Any

from fastapi import APIRouter

from src.core.controller import Controller
from src.core.middleware import Middleware


def route(router: APIRouter, path: str, methods: list[str], controller: Controller,
          middlewares: list[Middleware] = None):
    handle_func = controller.handle

    async def router_func(*args: Any, **kwargs: Any):
        if middlewares is None or len(middlewares) == 0:
            return await handle_func(*args, **kwargs)
        else:
            async def call_next(index: int):
                if index < len(middlewares):
                    return await middlewares[index].handle(
                        lambda: call_next(index + 1)
                    )
                else:
                    return await handle_func(*args, **kwargs)

            return await call_next(0)

    update_wrapper(router_func, handle_func)
    router_func.__signature__ = signature(handle_func)

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


def get(router: APIRouter, path: str, controller: Controller, middlewares: list[Middleware] = None):
    return route(router, path, ['get'], controller, middlewares)


def post(router: APIRouter, path: str, controller: Controller, middlewares: list[Middleware] = None):
    return route(router, path, ['post'], controller, middlewares)
