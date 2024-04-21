class HttpException(Exception):
    """
    The `HttpException` class is an exception used to represent HTTP errors.

    Attributes:
        status_code (int): The HTTP status code associated with the error.
        message (str): The error message.
        body (dict): The optional response body associated with the error.

    Methods:
        __init__(status_code: int, message: str, body: dict = None): Initializes a new instance of the HttpException class.

        Usage:
            raise HttpException(404, "Not Found", {"error": "Resource not found"})
    """

    def __init__(self, status_code: int, message: str, body: dict = None):
        if body is None:
            body = {}
        self.status_code = status_code
        self.message = message
        self.body = body


class InternalException(HttpException):
    """

    InternalException Class
    -----------------------

    :module: your_module_name

    :class: InternalException

    This class represents an internal server exception. It is a subclass of HttpException.

    Methods
    -------
    __init__(message: str)
        Initialize the InternalException class object with the given error message.

    Attributes
    ----------
    message : str
        The error message associated with the exception.

    """

    def __init__(self, message: str):
        super().__init__(500, message)


class GuardException(HttpException):
    """Represents an exception that occurs when a guard condition fails.

    Args:
        message (str): The error message associated with the exception.
        body (dict, optional): The error body associated with the exception. Defaults to None.

    Attributes:
        status_code (int): The HTTP status code associated with the exception.
        message (str): The error message associated with the exception.
        body (dict): The error body associated with the exception.

    """

    def __init__(self, message: str, body: dict = None):
        super().__init__(422, message, body)
