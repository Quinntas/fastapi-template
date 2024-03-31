from src.core.guard import against_none, against_less_than, against_greater_than


def user_password_validator(password: str) -> str:
    against_none("password", password)
    against_less_than("password", password, 6)
    against_greater_than("password", password, 20)
    return password
