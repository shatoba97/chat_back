from peewee import Model, SqliteDatabase
telegram_db = SqliteDatabase("telegram.db")

class BaseModel(Model):
    class Meta:
        database = telegram_db