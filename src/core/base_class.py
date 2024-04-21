from pydantic import BaseModel


class BaseClass(BaseModel):
    """

    This class represents a base class that extends the `BaseModel` class. It provides a configuration option to enable or disable assignment validation.

    Attributes:
        Config (class): A nested class that holds configuration options for the `BaseClass`.

    Example:
        class BaseClass(BaseModel):
            class Config:
                validate_assignment = True
    """

    class Config:
        validate_assignment = True
