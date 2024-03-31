from abc import ABC, abstractmethod

from peewee import Model

from src.core.base_domain import BaseDomain


class BaseMapper(ABC):
    def __init__(self, model: Model, domain: BaseDomain):
        self.model = model
        self.domain = domain

    @staticmethod
    def to_persistence(domain: BaseDomain):
        return {k: v for k, v in domain.__dict__.items() if v is not None}

    def to_domain(self, model: Model):
        return self.domain.cls(**model.__dict__)

    @abstractmethod
    def to_public_domain(self):
        pass
