""" Routing for authontification. """
from peewee import *
from flask.helpers import url_for
from flask import request, make_response
from auth.auth import decode_token, generate_token
from main import app

from model import User
from service.base_response import base_response


@app.route("/auth", methods=["POST"])
def auth():
    """Auth method for user."""
    print(url_for("auth"), "123", request.json)
    auth_request = request.authorization
    if not auth_request or not auth_request.username or not auth_request.password:
        return base_response(
            [],
            401,
            "could not verify",
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


@app.route("/register-user", methods=["POST"])
def sign_up():
    """Sign up method."""
    print(url_for("sign_up"))
    json = request.json
    if not json or not json["login"] or not json["password"]:
        make_response(
            "could not verify",
            401,
        )
    user_exist = bool(User.select().where(User.login == json["login"]).count())
    if user_exist:
        return make_response(
            dict(error="User exist"),
            401,
        )
    token = generate_token(json)
    user = User(
        login=json["login"],
        password=json["password"],
        chats=list(),
        token=token,
        nick_name=json["nickName"],
        first_name=json["firstName"],
        last_name=json["lastName"],
        icon=json["icon"] or '',
    )
    user.save()
    return dict({"token": token, "id": user.id})


@app.route("/user", methods=["GET"])
def get_user():
    """Get user by token."""
    print(url_for("get_user"))
    authorization: str = request.environ["HTTP_AUTHORIZATION"]
    if not authorization:
        return base_response([], 401, "Could not verify")

    token = authorization.replace("Bearer ", "")
    query = User.select().where(User.token == token)
    if not bool(len(query)):
        return base_response([], 401, "Token doesn`t valid")
    user = query[0]
    return base_response(dict(nick_name=user.login))


@app.route("/get-users", methods=["GET"])
def get_users():
    """Get list of all users for testing."""
    print(url_for("get_users"))
    collection = []
    query = User.select()
    for user in query:
        token = decode_token(user.token)
        if not token == {} and bool(token.get("password")):
            collection.append(
                dict(
                    {
                        "login": user.login,
                        "password": token.get("password"),
                        "chats": user.chats,
                        "token": user.token,
                    }
                )
            )
    return {"collection": collection}
