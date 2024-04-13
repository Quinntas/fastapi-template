from src.core.base_class import BaseClass


class UserCreateDTO(BaseClass):
    name: str
    email: str
    password: str
