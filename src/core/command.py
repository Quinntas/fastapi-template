from abc import ABCMeta, abstractmethod

from src.core.base_dto import BaseDTO


class Command(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, dto: BaseDTO, *args, **kwargs):
        pass
