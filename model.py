from peewee import BareField, CharField, Field, ForeignKeyField, IntegerField, Model
from main import telegram_db

class User(Model):
  login= CharField()
  password= CharField()
  public_id = IntegerField()
  chats= list()

  class Meta():
    database = telegram_db

  
User.create_table()
