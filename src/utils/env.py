from decouple import config

from src.core.base_class import BaseClass
from src.core.errors import InternalException


def get_env(env_name: str, required: bool = True, default_value: str = "") -> str:
    """
    Get the value of an environment variable.

    :param env_name: The name of the environment variable.
    :param required: Whether the environment variable is required. If set to True, an InternalException will be raised if the environment variable is not found. Default is True.
    :param default_value: The default value to return if the environment variable is not found and required is set to False. Default is an empty string.
    :return: The value of the environment variable as a string.
    """
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
    REDIS_HOST: str = get_env("REDIS_HOST")
    REDIS_PORT: int = int(get_env("REDIS_PORT", required=False, default_value="6379"))


env: Env = Env()
