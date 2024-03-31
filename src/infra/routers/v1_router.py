from fastapi import APIRouter

from src.core.middleware import middleware_wrapper
from src.modules.shared.useCases.health_check.health_check_usecase import health_check_usecase
from src.modules.user.infra.http.router.user_router import user_router

v1_router = APIRouter(
    route_class=middleware_wrapper(
        middleware_classes=[
            # ProcessTimeMiddleware
        ]
    ),
)

v1_router.get("/", tags=['Health Check'])(health_check_usecase)

v1_router.include_router(user_router)
