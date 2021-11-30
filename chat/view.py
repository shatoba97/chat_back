from main import app
from flask.helpers import url_for
from models.user import User
from models.user_chat import UserChat
from service.base_response import base_response

from service.token_service import token_req


@app.route("/chats", methods=["GET"])
@token_req
def get_all_chats(e):
    print(url_for("get_all_chats"), e)
    chats = (
        User.select()
        .join(UserChat, on=(UserChat.user_id == User.id))
        .where(UserChat.user_id == User.id)
        .first()
    )
    if chats:
        return base_response({})
    return base_response(None, 500, "No chats")
