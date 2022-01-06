from operator import and_
from chat.chat import register_chat
from main import app
from flask.helpers import url_for
from flask import request
from models.user import User
from models.chat import Chat
from models.user_chat import UserChat
from service.base_response import base_response

from service.token_service import token_req


@app.route("/chats", methods=["GET"])
@token_req
def get_all_chats(user: User):
    print(url_for("get_all_chats"), user)
    chats = (
        UserChat.select()
        .join(User)
        .where(UserChat.user.id == user.id)
    )
    
    if len(chats):
        return base_response(
            {
                "chats": [
                    {"chat_id": chat.id, "chat_name": chat.name_of_chat}
                    for chat in chats
                ]
            },
            200,
        )
    return base_response([], 200)


@app.route("/chat", methods=["POST"])
@token_req
def create_chats(user):
    print(url_for("create_chats"), user)
    chat_req = request.json
    return register_chat(user, chat_req)
    chats = User.select().join(UserChat, on=(UserChat.user_id == User.id)).first()
    if chats:
        return base_response({})
    return base_response(None, 500, "No chats")
