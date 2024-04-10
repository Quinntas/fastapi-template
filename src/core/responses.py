import json

from starlette.responses import Response


def dict_response(content: dict) -> dict:
    return content


def json_response(status_code: int, content: dict) -> Response:
    return Response(content=json.dumps(content), status_code=status_code, headers={"Content-Type": "application/json"})


def no_content_response() -> Response:
    return Response(status_code=204)
