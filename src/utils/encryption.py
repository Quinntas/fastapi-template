from __future__ import annotations

import hashlib

from passlib.hash import pbkdf2_sha256

from src.utils.env import env


def encrypt_with_sha256(content: str) -> str:
    encoded_string = (env.PEPER + content).encode()
    return hashlib.sha256(encoded_string).hexdigest()


def encrypt_with_pbkdf2_sha256(data: str) -> str:
    return pbkdf2_sha256.hash(env.PEPER + data, rounds=10000)


def verify_encryption(data: str, encrypted_str: str) -> bool:
    return pbkdf2_sha256.verify(env.PEPER + data, encrypted_str)
