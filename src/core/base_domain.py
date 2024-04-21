import datetime
from typing import Optional, Any, Annotated

from pydantic import ValidationInfo, ValidatorFunctionWrapHandler, ValidationError
from pydantic.functional_validators import WrapValidator

from src.core.base_class import BaseClass


def datetime_validator(
        v: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
) -> datetime.datetime:
    """
    Validate the given value `v` as a datetime.

    :param v: The value to be validated.
    :type v: Any
    :param handler: The handler function used to parse the datetime string.
    :type handler: ValidatorFunctionWrapHandler
    :param info: The validation information.
    :type info: ValidationInfo
    :return: The validated datetime value.
    :rtype: datetime.datetime
    :raises ValidationError: If the value does not match the required datetime format.
    """
    if info.mode == 'json':
        assert isinstance(v, str), 'str required'
        try:
            return handler(v)
        except ValidationError:
            raise ValidationError('datetime.datetime required')
    assert info.mode == 'python'
    assert isinstance(v, (str, datetime.datetime)), 'str or datetime required'
    return v


CustomDatetime = Annotated[datetime.datetime, WrapValidator(datetime_validator)]


class BaseDomain(BaseClass):
    """
    Represents a base domain class.

    :ivar id: The ID of the domain.
    :vartype id: Optional[int]
    :ivar pid: The PID of the domain.
    :vartype pid: Optional[str]
    :ivar createdAt: The creation datetime of the domain.
    :vartype createdAt: Optional[CustomDatetime]
    :ivar updatedAt: The update datetime of the domain.
    :vartype updatedAt: Optional[CustomDatetime]
    """
    id: Optional[int] = None
    pid: Optional[str] = None
    createdAt: Optional[CustomDatetime] = None
    updatedAt: Optional[CustomDatetime] = None
