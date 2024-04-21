from datetime import datetime

import jwt

from src.utils.env import env

EXP_KEY = 'exp'


def sign(payload: dict, expires: datetime) -> str:
    """
    Sign the payload with a expiration timestamp and return the encoded JWT.

    :param payload: A dictionary containing the data to be included in the JWT.
    :param expires: A `datetime` object representing the expiration date and time of the JWT.
    :return: A string representing the encoded JWT.
    """
    payload[EXP_KEY] = expires.timestamp()
    return jwt.encode(payload, env.JWT_SECRET, algorithm=env.JWT_ALGORITHM)


def decode(token: str) -> dict | None:
    """

    Decode the given token.

    :param token: The token to be decoded.
    :return: A dictionary containing the decoded token, or None if the token is invalid.
    """
    try:
        decode_token = jwt.decode(jwt=token, key=env.JWT_SECRET, algorithms=env.JWT_ALGORITHM)
        if decode_token[EXP_KEY] >= datetime.now().timestamp():
            del decode_token[EXP_KEY]
            return decode_token
        return None
    except jwt.exceptions.DecodeError:
        return None
