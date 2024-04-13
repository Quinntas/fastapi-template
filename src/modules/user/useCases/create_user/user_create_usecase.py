from __future__ import annotations

import uuid

from fastapi import Body
from starlette.responses import JSONResponse

from src.core.responses import json_response
from src.modules.user.domain.user import UserDomain
from src.modules.user.domain.value_objects.user_email import user_email_validator
from src.modules.user.domain.value_objects.user_name import user_name_validator
from src.modules.user.domain.value_objects.user_password import user_password_validator
from src.modules.user.repo.user_repo import user_repo
from src.modules.user.useCases.create_user.user_create_dto import UserCreateDTO
from src.utils.encryption import encrypt_with_pbkdf2_sha256


async def user_create_usecase(user: UserCreateDTO = Body(..., embed=False)) -> JSONResponse:
    email = user_email_validator(user.email)
    name = user_name_validator(user.name)
    password = user_password_validator(user.password)

    encrypted_password = encrypt_with_pbkdf2_sha256(password)

    user = UserDomain(
        name=name, email=email, password=encrypted_password, pid=str(uuid.uuid4())
    )

    user_repo.create(user)

    return json_response(status_code=201, content={
        "message": "User created successfully",
    })
