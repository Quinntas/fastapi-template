from fastapi import APIRouter

from src.core.middleware import middleware_wrapper
from src.modules.shared.useCases.health_check.health_check import health_check_use_case

v1_router = APIRouter(
    route_class=middleware_wrapper(
        middleware_classes=[
            # ProcessTimeMiddleware
        ]
    ),
)

v1_router.get("/", tags=['Utils'])(health_check_use_case)
