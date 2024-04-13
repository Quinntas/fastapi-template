from src.core.base_class import BaseClass


class UserLoginDTO(BaseClass):
    email: str
    password: str


class UserLoginResponseDTO(BaseClass):
    token: str
    expires: int
