from __future__ import annotations

from fastapi import APIRouter

from src.modules.user.useCases.create_user.user_create_usecase import user_create_usecase
from src.modules.user.useCases.user_login.user_login_usecase import user_login_usecase

user_router = APIRouter(tags=["User"], prefix="/users")

user_router.post("/create")(user_create_usecase)
user_router.post("/login")(user_login_usecase)
