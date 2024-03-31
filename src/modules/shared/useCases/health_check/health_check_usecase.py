from starlette.responses import Response

from src.core.responses import json_response


async def health_check_usecase() -> Response:
    return json_response(200, {"message": "ok"})
