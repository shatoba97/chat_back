from peewee import Model
from main import telegram_db

class BaseModel(Model):
    class Meta:
        database = telegram_db