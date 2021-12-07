""" Asd. """
from peewee import CharField, ForeignKeyField

from models.base import BaseModel
from models.user_chat import UserChat


class User(BaseModel):
    """Base user model."""

    login = CharField(unique=True)
    password = CharField()
    token = CharField(unique=True, null=True)
    nick_name = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    icon = CharField(null=True)
