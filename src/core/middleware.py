from abc import ABCMeta, abstractmethod
from collections.abc import Awaitable

from src.core.typings import next_func


class Middleware(metaclass=ABCMeta):
    @abstractmethod
    async def handle(self, call_next: next_func) -> Awaitable[None]:
        pass
