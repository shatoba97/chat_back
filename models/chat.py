from peewee import CharField, ForeignKeyAccessor, ForeignKeyField
from models.base import BaseModel

class Chat(BaseModel):
    name_of_chat = CharField()
    icon = CharField(null=True)
