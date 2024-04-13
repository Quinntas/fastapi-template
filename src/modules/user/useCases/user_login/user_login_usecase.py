import datetime

from fastapi import Body
from starlette.responses import JSONResponse

from src.core.responses import json_response
from src.infra.database.redis.redis_connection import redis_client
from src.modules.user.domain.user import UserModel
from src.modules.user.domain.value_objects.user_email import user_email_validator
from src.modules.user.domain.value_objects.user_password import user_password_validator
from src.modules.user.repo.user_repo import user_repo
from src.modules.user.useCases.user_login.user_login_constants import SESSION_EXPIRATION_TIME
from src.modules.user.useCases.user_login.user_login_dto import UserLoginDTO, UserLoginResponseDTO
from src.utils.encryption import verify_encryption
from src.utils.jsonwebtoken import sign


async def user_login_usecase(user: UserLoginDTO = Body(..., embed=False)) -> JSONResponse:
    email = user_email_validator(user.email)
    password = user_password_validator(user.password)

    user = user_repo.select_one(
        (UserModel.email == email)
    )

    if not user:
        return json_response(status_code=404, content={
            "message": "User not found"
        })

    if not verify_encryption(password, user.password):
        return json_response(status_code=401, content={
            "message": "Credentials do not match"
        })

    public_jwt = sign({
        "pid": user.pid,
    }, datetime.datetime.now() + datetime.timedelta(seconds=SESSION_EXPIRATION_TIME))

    private_jwt = sign({
        "id": user.id,
        "pid": user.pid,
        "email": user.email,
        "name": user.name,
    }, datetime.datetime.now() + datetime.timedelta(seconds=SESSION_EXPIRATION_TIME))

    redis_client.set(f"session:{user.pid}", private_jwt, SESSION_EXPIRATION_TIME)

    return json_response(status_code=200, content=UserLoginResponseDTO(
        token=public_jwt,
        expires=SESSION_EXPIRATION_TIME
    ))
