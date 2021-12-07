from peewee import CharField, ForeignKeyAccessor, ForeignKeyField
from models.base import BaseModel
from models.user_chat import UserChat


class Chat(BaseModel):
    name_of_chat = CharField()
    icon = CharField(null=True)
    userid = ForeignKeyField(UserChat, null=True, to_field="user_id")
