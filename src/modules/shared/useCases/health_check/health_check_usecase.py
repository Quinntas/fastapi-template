from starlette.responses import JSONResponse

from src.core.responses import json_response


async def health_check_usecase() -> JSONResponse:
    return json_response(status_code=200, content={
        "message": "I'm alive",
    })
