from src.core.guard import against_none, against_less_than, against_greater_than


def user_name_validator(name: str) -> str:
    against_none("name", name)
    against_less_than("name", name, 3)
    against_greater_than("name", name, 50)
    return name.upper()
