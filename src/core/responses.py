from starlette.responses import Response, JSONResponse

from src.core.base_class import BaseClass


def dict_response(content: dict) -> dict:
    """
    This method takes in a dictionary as input and returns the same dictionary.

    :param content: A dictionary object to be returned.
    :type content: dict
    :return: The same dictionary object that was passed as input.
    :rtype: dict
    """
    return content


def json_response(status_code: int, content: dict | BaseClass) -> JSONResponse:
    """
    Create a JSON response object.

    :param status_code: An integer representing the HTTP status code.
    :param content: A dictionary or an instance of `BaseClass` representing the content of the response.
    :return: A `JSONResponse` object.

    The `JSONResponse` object is created with the provided `status_code` and `content`. If `content` is an instance of `BaseClass`, it is converted to a dictionary using the `dict()` method before being passed as the content.

    Example usage:
    ```
    response = json_response(200, {'message': 'Success'})
    ```
    """
    return JSONResponse(status_code=status_code,
                        content=content.dict() if isinstance(content, BaseClass) else content,
                        media_type="application/json")


def no_content_response() -> Response:
    """
    :return: A Response object with a status code of 204 indicating a successful request with no content.
    """
    return Response(status_code=204)
