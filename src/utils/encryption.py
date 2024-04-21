from __future__ import annotations

import hashlib

from passlib.hash import pbkdf2_sha256

from src.utils.env import env


def encrypt_with_sha256(content: str) -> str:
    """
    Encrypts the given content using SHA256 algorithm.

    :param content: The content to be encrypted.
    :return: The SHA256 hash value of the encrypted content.
    """
    encoded_string = (env.PEPER + content).encode()
    return hashlib.sha256(encoded_string).hexdigest()


def encrypt_with_pbkdf2_sha256(data: str) -> str:
    """
    Encrypts the given data using the PBKDF2_SHA256 algorithm.

    :param data: The data to be encrypted.
    :type data: str
    :return: The encrypted string.
    :rtype: str
    """
    return pbkdf2_sha256.hash(env.PEPER + data, rounds=10000)


def verify_encryption(data: str, encrypted_str: str) -> bool:
    """
    Verify Encryption using constant time comprarison

    Verifies if the given data matches the encrypted string.

    :param data: The data to verify.
    :type data: str
    :param encrypted_str: The encrypted string to match.
    :type encrypted_str: str
    :return: True if the data matches the encrypted string, False otherwise.
    :rtype: bool

    Example Usage:
    >>> data = "Hello, World!"
    >>> encrypted_str = "$pbkdf2-sha256$29000$VHV1ckMY6ZdYBgSQKwooDQ$h6B/+gRVTk4j8bPI657HIhBRTvOMBx1RWF8bRxy+lVc"
    >>> verify_encryption(data, encrypted_str)
    True

    """
    return pbkdf2_sha256.verify(env.PEPER + data, encrypted_str)
