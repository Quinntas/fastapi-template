import datetime
from typing import Optional, Any, Annotated

from pydantic import ValidationInfo, ValidatorFunctionWrapHandler, ValidationError
from pydantic.functional_validators import WrapValidator

from src.core.base_class import BaseClass


def datetime_validator(
        v: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
) -> datetime.datetime:
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
    id: Optional[int] = None
    pid: Optional[str] = None
    createdAt: Optional[CustomDatetime] = None
    updatedAt: Optional[CustomDatetime] = None
