from peewee import CharField
from models.base import BaseModel

class Chat(BaseModel):
    name_of_chat = CharField()
    icon = CharField(null=True)
