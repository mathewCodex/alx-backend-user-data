#!/usr/bin/env python3
"""A mod encrypting password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password using a random salt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password:  str) -> bool:
    """Checks is a hashed password formed from the given pass
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
