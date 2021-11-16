""" asd """
import datetime
from typing import Any, Dict, Union
from flask.helpers import make_response
from flask.wrappers import Response
import jwt
from werkzeug.datastructures import Authorization
from model import User
from config import config
from service.base_response import base_response

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
            "password": user['password'],
        }
        token: str = jwt.encode(payload, key=config.get("SECRET_KEY"),)
        return token
    except RuntimeError:
        return 'error'


def decode_token(token: str):
    """Decode token, get payload from token

    Args:
        token (str): token

    Returns:
        Dict[]: User data
    """
    try:
        payload: Dict[str, str] = jwt.decode(token, key=config.get('SECRET_KEY'), algorithms="HS256")
        print('payload', payload)
        return payload
    except RuntimeError:
        a: Dict[str, str] = dict()
        return a

def authorize(auth_request: Union[Authorization, None]):
    """ Api method for authorize user. 

    Args:
        auth_request (Union[Authorization, None]): Authorization user data

    Returns:
        Responce: Auth responce
    """
    if not auth_request or not auth_request.username or not auth_request.password:
        return base_response(
            [],
            400,
            "Could not verify",
        )

    users = User.select().where(User.login == auth_request.username)
    if not bool(users.count()):
        return make_response(
            dict(error="User with this login doesn`t exist"),
            200,
        )
    user: User = users[0]
    password = decode_token(user.token).get("password")
    if password == user.password:
        return base_response(
            dict(token=user.token, id=user.id),
            200,
        )
    return make_response(
        dict(error="Not correct login or password"),
        200,
    )

def register_user(user_req: Dict[str, str]):
    """ Sign up method.

    Args:
        user_req (Dict[str, str]): User data from request

    Returns:
        Response [Dict[str, str]]: Return token and id of new user
    """
    if not user_req or not user_req["login"] or not user_req["password"]:
        return make_response(
            "could not verify",
            204,
        )
    user_exist = bool(User.select().where(User.login == user_req["login"]).count())
    if user_exist:
        return make_response(
            dict(error="User exist"),
            200,
        )
    token = generate_token(user_req)
    user = User(
        login=user_req["login"],
        password=user_req["password"],
        chats=list(),
        token=token,
        nick_name=user_req["nickName"],
        first_name=user_req["firstName"],
        last_name=user_req["lastName"],
        icon=user_req["icon"] or '',
    )
    user.save()
    return base_response(dict({"token": token, "id": user.id}))









def get_user(authorization_data):
    if not authorization_data:
        return base_response([], 401, "Could not verify")

    token = authorization_data.replace("Bearer ", "")
    query = User.select().where(User.token == token)
    if not bool(len(query)):
        return base_response([], 401, "Token doesn`t valid")
    user = query[0]
    return base_response(dict(nick_name=user.login))