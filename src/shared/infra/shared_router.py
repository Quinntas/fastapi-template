from fastapi import APIRouter

from src.core.routes import get
from src.shared.resources.health_check import health_check_controller

shared_router = APIRouter()

get(shared_router, '/', health_check_controller)
