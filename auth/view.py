""" Routing for authontification. """
from peewee import *
from flask.helpers import url_for
from flask import request, make_response
from auth.auth import decode_token, generate_token, authorize, get_user, register_user
from main import app

from model import User
from service.base_response import base_response


@app.route("/auth", methods=["POST"])
def auth():
    """Auth method for user."""
    print(url_for("auth"), request.json)
    return authorize(request.authorization)


@app.route("/register-user", methods=["POST"])
def sign_up():
    """Sign up method."""
    print(url_for("sign_up"))
    user_req = request.json
    return register_user(user_req)
#######################################################




@app.route("/user", methods=["GET"])
def get_user_fake_req():
    """Get user by token."""
    print(url_for("get_user_fake_req"))
    authorization_data: str = request.environ["HTTP_AUTHORIZATION"]
    get_user(authorization_data)


@app.route("/get-users", methods=["GET"])
def get_users_fake_req():
    """Get list of all users for testing."""
    print(url_for("get_users_fake_req"))
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
