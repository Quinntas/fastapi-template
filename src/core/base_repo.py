from __future__ import annotations

from abc import ABC

from peewee import IntegrityError
from peewee import Model

from src.core.base_domain import BaseDomain
from src.core.base_mapper import BaseMapper
from src.core.errors import HttpException


class BaseRepo(ABC):
    """
    :class: BaseRepo

    The BaseRepo class is an abstract base class that provides a basic implementation for interacting with a database table.

    :param model: The model class representing the database table.
    :type model: type[Model]
    :param mapper: The mapper class used for converting domain objects to persistence objects and vice versa.
    :type mapper: BaseMapper

    """

    def __init__(self, model: type[Model], mapper: BaseMapper):
        self.model: type[Model] = model
        self.mapper: BaseMapper = mapper

    def create(self, domain: type[type[BaseDomain]]):
        """
        :param domain: The domain object to be created.
        :return: The created domain object.
        """
        try:
            return self.model.create(**self.mapper.to_persistence(domain))
        except IntegrityError as e:
            raise HttpException(409, e.args[1])

    def select_one(self, where: dict):
        """
        Selects a single record from the database table based on the specified conditions.

        :param where: A dictionary representing the conditions to be applied in the query.
        :type where: dict
        :return: The selected record converted to the domain object.
        :rtype: object or None
        """
        q = self.model.select().where(where)
        if q.count() == 0:
            return None
        return self.mapper.to_domain(q[0])

    def select(self, where: dict):
        """
        Selects records from the model based on the given conditions.

        :param where: A dictionary specifying the conditions to be used in the WHERE clause of the SQL SELECT statement.
                      The dictionary should have column names as keys and the corresponding values to filter the records.

        :return: A query object representing the SQL SELECT statement with the specified conditions applied.
        """
        return self.model.select().where(where)
