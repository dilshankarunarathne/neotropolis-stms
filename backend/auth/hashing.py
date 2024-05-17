from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

import config

from services.token_service import add_token_to_blacklist, check_if_token_is_blacklisted

"""
    middleware for hashing passwords and creating tokens
"""

SECRET_KEY = config.get("security", "security.secretkey")
ALGORITHM = config.get("security", "security.algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def blacklist_token(token):
    add_token_to_blacklist(token)


def is_token_blacklisted(token):
    return check_if_token_is_blacklisted(token)
