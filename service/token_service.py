from functools import wraps
from typing import Dict
from flask import request
import jwt
from jwt import ExpiredSignatureError, DecodeError
from config import config
from models.user import User
from flask import request
import datetime

from service.base_response import base_response


def token_req(func):
    @wraps(func)
    def decorator(*args, **kargs):
        token = None
        if not request.environ.get("HTTP_AUTHORIZATION") or not request.environ.get(
            "HTTP_AUTHORIZATION"
        ).count("Bearer"):
            base_response([], 401, "Token is invalid")

        token = request.environ.get("HTTP_AUTHORIZATION").replace("Bearer ", "")
        if token:
            try:
                data = decode_token(token)
                if token_expired(data):
                    return base_response([], 401, "Invalid token")
                user = User.select().where(User.id == data.get("id")).get()
                if not user:
                    return base_response([], 401, "Invalid token")
                return func(user, *args, **kargs)
            except Exception as error:
                print(error)
                return base_response([], 401, "Invalid token")
        return base_response([], 401, "You dont sent token")

    return decorator


def token_expired(token: str) -> bool:
    return False


def generate_token(user: Dict[str, str]):
    """Generate token for user

    Args:
        user (Dict[str, str]): User data

    Returns:
        str: Return token
    """
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            "iat": datetime.datetime.utcnow(),
            "password": user.password,
            "id": user.id,
        }
        token: str = jwt.encode(
            payload,
            key=config.get("SECRET_KEY"),
        )
        return token
    except RuntimeError:
        return "error"


def decode_token(token: str) -> Dict[str, str]:
    """Decode token, get payload from token
    Args:
        token (str): token
    Returns:
        Dict[]: User data
    """
    try:
        if not token:
            a: Dict[str, str] = dict(password="", expired=True)
            return a
        payload: Dict[str, str] = jwt.decode(
            token, key=config.get("SECRET_KEY"), algorithms="HS256"
        )
        print("payload", dict(password=payload.get("password"), expired=False))
        return payload
    except RuntimeError or DecodeError or ExpiredSignatureError:
        a: Dict[str, str] = dict(password="", expired=True)
        return a
