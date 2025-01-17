class HttpException(Exception):
    def __init__(self,
                 message: str,
                 status_code: int,
                 errors: list[dict] = None
                 ):
        self.message = message
        self.status_code = status_code
        self.errors = errors

    def to_dict(self):
        return {
            "message": self.message,
            "errors": self.errors
        }
