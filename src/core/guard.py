from src.core.errors import GuardException


def against_none(key: str, value: any) -> None:
    """
    Check if a value is None and raises an exception if it is.

    :param key: The key or name of the parameter being checked.
    :param value: The value being checked.
    :return: None
    :raises GuardException: Raised if `value` is None.

    """
    if value is None:
        raise GuardException(f"{key} is required")


def against_empty_string(key: str, value: str) -> None:
    """
    :param key: The name of the key that is being checked.
    :param value: The value associated with the key.
    :return: None
    """
    if value == "":
        raise GuardException(f"{key} is required")


def against_less_than(key: str, value: int | str, min_value: int) -> None:
    """
    Check if a value is greater than or equal to a minimum value.

    :param key: The key or name of the value being checked.
    :type key: str
    :param value: The value being checked. If it is a string, the length of the string will be used.
    :type value: int or str
    :param min_value: The minimum value that `value` should be greater than or equal to.
    :type min_value: int
    :raises GuardException: If `value` is less than `min_value`.
    :return: None
    :rtype: None
    """
    if isinstance(value, str):
        value = len(value)
    if value < min_value:
        raise GuardException(f"{key} must be greater than {min_value}")


def against_greater_than(key: str, value: int | str, max_value: int) -> None:
    """
    Check if the given value is greater than the maximum value.

    :param key: A string representing the key or name of the value.
    :param value: An integer or string representing the value to be checked.
                  In case of a string, the length is used for comparison.
    :param max_value: An integer representing the maximum allowed value.
    :return: None
    :raises GuardException: If the value is greater than the max_value.
    """
    if isinstance(value, str):
        value = len(value)
    if value > max_value:
        raise GuardException(f"{key} must be less than {max_value}")
