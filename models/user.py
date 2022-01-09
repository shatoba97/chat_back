""" Asd. """
from peewee import CharField

from models.base import BaseModel


class User(BaseModel):
    """Base user model."""
    login = CharField(unique=True)
    password = CharField()
    token = CharField(unique=True, null=True)
    nick_name = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    icon = CharField(null=True)
    
