from starlette.requests import Request
from starlette.responses import Response

from src.core.responses import json_response


async def health_check_use_case(request: Request, response: Response):
    return json_response(200, {"message": "ok"})
