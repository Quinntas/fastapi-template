from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from peewee import Model

from src.core.base_domain import BaseDomain


class BaseMapper(ABC):
    """

    :class: BaseMapper

    The `BaseMapper` class is an abstract base class that provides common methods and functionality for mapping between domain objects and persistence representations.

    Constructor:
        - `__init__(self, model: type[Model], domain: type[BaseDomain])`: Initializes a new instance of the `BaseMapper` class with the specified model and domain types.

    Static Method:
        - `to_persistence(domain: type[BaseDomain]) -> dict`: Converts a domain object to its persistence representation. Returns the persistence representation of the domain object.

    Methods:
        - `to_domain(self, model: type[Model]) -> domain object`: Converts a model object to a domain object. Returns the domain object created from the model object.
        - `to_public_domain(self) -> None`: Converts the object to the public domain and removes any restrictions. Does not return a value.

    Please note that `BaseMapper` is an abstract base class and should not be instantiated directly. Subclasses of `BaseMapper` should provide implementations for the abstract methods.

    """

    def __init__(self, model: type[Model], domain: type[BaseDomain]):
        self.model: type[Model] = model
        self.domain: type[BaseDomain] = domain

    @staticmethod
    def to_persistence(domain: type[BaseDomain]):
        """
        Converts a domain object to its persistence representation.

        :param domain: The domain object to be converted.
        :return: The persistence representation of the domain object.
        """
        return {k: v for k, v in domain.__dict__.items() if v is not None}

    def to_domain(self, model: type[Model]):
        """
        Convert a model object to a domain object.

        :param model: The model object to be converted.
        :type model: type[Model]
        :return: The domain object created from the model object.
        :rtype: domain object
        """
        return self.domain(**model.__dict__['__data__'])

    @abstractmethod
    def to_public_domain(self):
        """
        Converts the object to the public domain and removes any restrictions.

        :return: None
        """
        pass
