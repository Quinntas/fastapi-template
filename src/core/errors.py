class HttpException(Exception):
    def __init__(self, status_code: int, message: str, body: dict = None):
        if body is None:
            body = {}
        self.status_code = status_code
        self.message = message
        self.body = body


class InternalException(HttpException):
    def __init__(self, message: str):
        super().__init__(500, message)


class GuardException(HttpException):
    def __init__(self, message: str, body: dict = None):
        super().__init__(422, message, body)
