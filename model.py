""" Asd. """
from peewee import CharField, Model
from main import telegram_db

class User(Model):
    """ Base user model. """
    login = CharField()
    password = CharField()
    token = CharField()
    chats = list()
    def __init__(self, *args) -> None:
        print(args)
    class Meta:
        database = telegram_db


User.create_table()
