from peewee import ForeignKeyField, IntegerField
from models.base import BaseModel
from models.chat import Chat
from models.user import User


class UserChat(BaseModel):
    """Connect 2 tables chat and user"""

    chat = ForeignKeyField(Chat, unique=False)
    user = ForeignKeyField(User, unique=False)
