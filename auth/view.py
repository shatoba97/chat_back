from flask.helpers import url_for
from flask import request, jsonify, make_response
from auth.auth import decode_token, generate_token
from main import app
from peewee import *

from model import User


@app.route("/auth", methods=["POST"])
def auth():
    """Asd."""
    print(url_for("auth"), request.json)
    auth_request = request.authorization
    if not auth_request or not auth_request.username or not auth_request.password:
        make_response(
            "could not verify",
            401,
            {"WWW.Authentication": 'Basic realm: "login required"'},
        )

    users = User.select().where(User.login == auth_request.username)

    return dict(
        users=
        [
            {
                "login": user.login,
                "password": user.password,
                "chats": user.chats,
                "token": user.token,
            }
            for user in users
        ],
    )


@app.route("/register", methods=["POST"])
def sign_up():
    """Sign up method."""
    print(url_for("sign_up"))
    json = request.json
    if not json or not json["login"] or not json["password"]:
        make_response(
            "could not verify",
            401,
            {"WWW.Authentication": 'Basic realm: "login required"'},
        )
    # user_exist = User.select().where(User.login == json["login"]).get()
    token = generate_token(json)
    user = User(
        login=json["login"],
        password=json["password"],
        chats=list(),
        token=token,
    )
    user.save()
    return dict({"token": token, "id": user.id})


@app.route("/get-users", methods=["GET"])
def get_users():
    """Asd."""
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
