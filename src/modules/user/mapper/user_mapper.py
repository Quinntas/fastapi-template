from src.core.base_mapper import BaseMapper
from src.modules.user.domain.user import User, UserModel


class UserMapper(BaseMapper):
    def __init__(self):
        super().__init__(UserModel, User)

    def to_public_domain(self):
        pass


user_mapper = UserMapper()
