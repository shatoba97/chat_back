""" asd """
import datetime
from typing import Dict, Union
from flask.helpers import make_response
from werkzeug.datastructures import Authorization
from models.user import User
from config import config
from service.base_response import base_response
from service.token_service import decode_token, generate_token


def authorize(auth_request: Union[Authorization, None]):
    """Api method for authorize user.
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
    """Sign up method.
    Args:
        user_req (Dict[str, str]): User data from request
    Returns:
        Response [Dict[str, str]]: Return token and id of new user
    """
    if not user_send_correct_data(user_req):
        return make_response(
            "could not verify",
            204,
        )
    user_exists = User.select().where(User.login == user_req["login"]).exists()
    if user_exists:
        return make_response(
            dict(error="User exist"),
            200,
        )
    user = User(
        login=user_req["login"],
        password=user_req["password"],
        nick_name=user_req.get("nickName"),
        first_name=user_req.get("firstName"),
        last_name=user_req.get("lastName"),
        icon=user_req.get("icon"),
    )
    user.save()
    token = generate_token(user)
    user.token = token
    user.save()
    return base_response(dict({"token": token, "id": user.id}))


def user_send_correct_data(user: dict) -> bool:
    return user and "login" in user and "password" in user


def get_user(authorization_data):
    if not authorization_data:
        return base_response([], 401, "Could not verify")

    token = authorization_data.replace("Bearer ", "")
    query = User.select().where(User.token == token)
    if not bool(len(query)):
        return base_response([], 401, "Token doesn`t valid")
    user = query[0]
    return base_response(dict(nick_name=user.login))
