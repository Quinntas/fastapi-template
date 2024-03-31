from src.core.base_class import BaseClass


class CreateUserDTO(BaseClass):
    name: str
    email: str
    password: str
