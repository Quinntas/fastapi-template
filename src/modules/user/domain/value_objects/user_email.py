from src.core.guard import against_none, against_less_than, against_greater_than


def user_email_validator(email: str) -> str:
    against_none("email", email)
    against_less_than("email", email, 3)
    against_greater_than("email", email, 50)
    return email
