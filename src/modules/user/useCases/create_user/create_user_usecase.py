from __future__ import annotations

import uuid

from fastapi import Body
from starlette.responses import Response

from src.core.responses import no_content_response
from src.modules.user.domain.user import User
from src.modules.user.domain.value_objects.user_email import user_email_validator
from src.modules.user.domain.value_objects.user_name import user_name_validator
from src.modules.user.domain.value_objects.user_password import user_password_validator
from src.modules.user.repo.user_repo import user_repo
from src.modules.user.useCases.create_user.create_user_dto import CreateUserDTO
from src.utils.encryption import encrypt_with_pbkdf2_sha256


async def create_user_usecase(user: CreateUserDTO = Body(..., embed=False)) -> Response:
    email = user_email_validator(user.email)
    name = user_name_validator(user.name)
    password = user_password_validator(user.password)

    encrypted_password = encrypt_with_pbkdf2_sha256(password)

    user = User(
        name=name, email=email, password=encrypted_password, pid=str(uuid.uuid4())
    )

    user_repo.create(user)

    return no_content_response()
