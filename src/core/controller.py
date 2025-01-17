from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Optional, Awaitable


class Controller(metaclass=ABCMeta):
    def __init__(self,
                 status_code: int = 200,
                 summary: Optional[str] = None,
                 description: Optional[str] = None,
                 deprecated: bool = False,
                 tags: Optional[list[str | Enum]] = None,
                 ):
        self.status_code = status_code
        self.summary = summary or self.__class__.__name__
        self.description = description
        self.name = self.summary
        self.deprecated = deprecated
        self.tags = tags

    @abstractmethod
    async def handle(self, *args, **kwargs) -> Awaitable[str | bytes | dict]:
        pass
