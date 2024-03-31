from src.core.errors import GuardException


def against_none(key: str, value: any) -> None:
    if value is None:
        raise GuardException(f"{key} is required")


def against_empty_string(key: str, value: str) -> None:
    if value == "":
        raise GuardException(f"{key} is required")


def against_less_than(key: str, value: int | str, min_value: int) -> None:
    if isinstance(value, str):
        value = len(value)
    if value < min_value:
        raise GuardException(f"{key} must be greater than {min_value}")


def against_greater_than(key: str, value: int | str, max_value: int) -> None:
    if isinstance(value, str):
        value = len(value)
    if value > max_value:
        raise GuardException(f"{key} must be less than {max_value}")
