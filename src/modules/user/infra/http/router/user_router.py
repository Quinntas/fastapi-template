from fastapi import APIRouter

from src.modules.user.useCases.create_user.create_user_usecase import create_user_usecase

user_router = APIRouter(tags=['User'], prefix="/users")

user_router.post("/")(create_user_usecase)
