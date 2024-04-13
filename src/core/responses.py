from starlette.responses import Response, JSONResponse

from src.core.base_class import BaseClass


def dict_response(content: dict) -> dict:
    return content


def json_response(status_code: int, content: dict | BaseClass) -> JSONResponse:
    return JSONResponse(status_code=status_code,
                        content=content.dict() if isinstance(content, BaseClass) else content,
                        media_type="application/json")


def no_content_response() -> Response:
    return Response(status_code=204)
