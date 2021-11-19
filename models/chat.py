from peewee import CharField, ForeignKeyAccessor
from models.base import BaseModel
from models.user_chat import UserChat


class Chat(BaseModel):
    name_of_chat = CharField()
    icon = CharField(null=True)
    userid = ForeignKeyAccessor(UserChat, backref='user')
