""" asd """
import datetime
from typing import Dict
import jwt
from config import config

def generate_token(user: Dict[str, str]) -> str:
    """Asd."""
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            "iat": datetime.datetime.utcnow(),
            "password": user['password'],
        }
        token = jwt.encode(payload, key=config.get("SECRET_KEY"),)
        return token
    except Exception as error:
        return ''


def decode_token(token: str) -> dict:
    """Asd."""
    try:
        payload = jwt.decode(token, key=config.get('SECRET_KEY'), algorithms="HS256")
        print('payload', payload)
        return payload
    except Exception as error:
        return dict()