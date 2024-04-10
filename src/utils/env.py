from decouple import config

from src.core.base_class import BaseClass
from src.core.errors import InternalException


def get_env(env_name: str, required: bool = True, default_value: str = "") -> str:
    try:
        return config(env_name)
    except:
        if required:
            raise InternalException(f"Environment variable {env_name} not found")
        return default_value


class Env(BaseClass):
    PORT: int = int(get_env("PORT", default_value="8000"))
    DATABASE_URL: str = get_env("DATABASE_URL")
    JWT_SECRET: str = get_env("JWT_SECRET")
    JWT_ALGORITHM: str = get_env("JWT_ALGORITHM")
    PEPER: str = get_env("PEPPER")


env: Env = Env()
