import datetime
from typing import Optional

from src.core.base_class import BaseClass


class BaseDomain(BaseClass):
    id: Optional[int] = None
    pid: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    updatedAt: Optional[datetime.datetime] = None
