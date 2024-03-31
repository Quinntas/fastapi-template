from decouple import config

from src.core.base_class import BaseClass


def get_env(env_name: str, required: bool = True, default_value: str = "") -> str:
    try:
        return config(env_name)
    except:
        if required:
            raise Exception(f"Environment variable {env_name} not found")
        return default_value


class Env(BaseClass):
    PORT: int = int(get_env("PORT", default_value="8000"))


env: Env = Env()
