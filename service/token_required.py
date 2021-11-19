from functools import wraps
from flask import request, jsonify
import jwt
import config
from models.user import User


def token_req(func):
    @wraps(func)
    def decorator(*args, **kargs):
        token = None
        return func("c", *args, **kargs)

    return decorator


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]

        if not token:
            return jsonify({"message": "a valid token is missing"})

        try:
            data = jwt.decode(token, config["SECRET_KEY"])
            current_user = User.query.filter_by(public_id=data["public_id"]).first()
        except:
            return jsonify({"message": "token is invalid"})

        return f(current_user, *args, **kwargs)

    return decorator
