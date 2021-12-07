from typing import Dict
from flask.wrappers import Response
from peewee import Expression
from models.user import User
from service.base_response import base_response


from models.chat import Chat
from models.user_chat import UserChat


def register_chat(user: User, chat: Dict[str, str]) -> Response:
    if not chat and not chat.name_of_chat:
        return base_response(
            None,
            500,
            "Bad request",
        )
    try:
        chat_db = Chat(
            name_of_chat=chat.get("chatName"), icon=chat.get("icon"), userid=user.id
        )
        chat_db.save()
        UserChat.create(chat_id=chat_db.id, user_id=user.id)
    except Exception as error:
        print(error)

    return base_response(
        {"chat_id": chat_db.id},
        200,
    )
