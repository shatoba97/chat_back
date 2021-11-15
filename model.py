""" Asd. """
from peewee import CharField, Model
from main import telegram_db

class User(Model):
    """ Base user model. """
    login = CharField()
    password = CharField()
    token = CharField()
    chats = list()
    nick_name = CharField()
    first_name = CharField()
    last_name = CharField()
    icon = CharField()
    class Meta:
        database = telegram_db


User.create_table()
