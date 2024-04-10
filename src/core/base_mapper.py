from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from peewee import Model

from src.core.base_domain import BaseDomain


class BaseMapper(ABC):
    def __init__(self, model: type[Model], domain: type[BaseDomain]):
        self.model: type[Model] = model
        self.domain: type[BaseDomain] = domain

    @staticmethod
    def to_persistence(domain: type[BaseDomain]):
        return {k: v for k, v in domain.__dict__.items() if v is not None}

    def to_domain(self, model: type[Model]):
        return self.domain.cls(**model.__dict__)

    @abstractmethod
    def to_public_domain(self):
        pass
