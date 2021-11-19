from peewee import IntegerField
from models.base import BaseModel


class UserChat(BaseModel):
    """Connect 2 tables chat and user"""

    chat_id = IntegerField(unique=True)
    user_id = IntegerField(unique=True)
