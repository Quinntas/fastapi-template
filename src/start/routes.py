from fastapi import APIRouter

from src.shared.infra.shared_router import shared_router

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(shared_router)
