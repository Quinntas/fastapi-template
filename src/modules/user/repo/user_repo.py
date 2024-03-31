from src.core.base_repo import BaseRepo
from src.modules.user.domain.user import UserModel
from src.modules.user.mapper.user_mapper import user_mapper


class UserRepo(BaseRepo):
    def __init__(self):
        super().__init__(UserModel, user_mapper)


user_repo = UserRepo()
