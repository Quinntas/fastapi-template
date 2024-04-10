from datetime import datetime

import jwt

from src.utils.env import env

EXP_KEY = 'exp'


def sign(payload: dict, expires: datetime) -> str:
    payload[EXP_KEY] = expires.timestamp()
    return jwt.encode(payload, env.JWT_SECRET, algorithm=env.JWT_ALGORITHM)


def decode(token: str) -> dict | None:
    try:
        decode_token = jwt.decode(jwt=token, key=env.JWT_SECRET, algorithms=env.JWT_ALGORITHM)
        if decode_token[EXP_KEY] >= datetime.now().timestamp():
            del decode_token[EXP_KEY]
            return decode_token
        return None
    except jwt.exceptions.DecodeError:
        return None
