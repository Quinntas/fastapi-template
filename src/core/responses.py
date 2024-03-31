import json

from starlette.responses import Response


def json_response(status_code: int, content: dict):
    return Response(content=json.dumps(content), status_code=status_code, headers={"Content-Type": "application/json"})


def no_content_response():
    return Response(status_code=204)
