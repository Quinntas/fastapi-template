import datetime
from typing import Optional

from src.core.base_class import BaseClass


class BaseDomain(BaseClass):
    id: Optional[int] = None
    pid: Optional[str] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
