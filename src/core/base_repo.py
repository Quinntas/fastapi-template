from abc import ABC

from peewee import Model, IntegrityError

from src.core.base_domain import BaseDomain
from src.core.base_mapper import BaseMapper
from src.core.errors import HttpException


class BaseRepo(ABC):
    def __init__(self, model: Model, mapper: BaseMapper):
        self.model: Model = model
        self.mapper: BaseMapper = mapper

    def create(self, domain: BaseDomain):
        try:
            return self.model.create(**self.mapper.to_persistence(domain))
        except IntegrityError as e:
            raise HttpException(409, e.args[1])
