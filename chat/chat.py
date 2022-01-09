from typing import Dict
from flask.wrappers import Response
from peewee import Expression, IntegrityError
from models.user import User
from service.base_response import base_response


from models.chat import Chat
from models.user_chat import UserChat


def register_chat(user: User, chat_req: Dict[str, str]) -> Response:
    if not chat_req and not chat_req.name_of_chat:
        return base_response(
            None,
            500,
            "Bad request",
        )
    try:
        chat_db = Chat(
            name_of_chat=chat_req.get("chatName"), icon=chat_req.get("icon"), userid=user.id
        )
        chat_db.save()
        userChat = UserChat(chat=chat_db, user=user)
        userChat.save()
    except (Exception, IntegrityError) as error:
        print(error)

    return base_response(
        {"chat_id": chat_db.id},
        200,
    )
