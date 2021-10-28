from typing import List, TypedDict
from flask import Flask, url_for, request
from peewee import *

telegram_db = SqliteDatabase('telegram.db')

app = Flask(__name__)

from auth.view import *

# @app.before_request
# def before_request():
#   telegram_db.connect()
# @app.errorhandler()
# def handle_exception(e):
#   print(e)

if __name__ == '__main__':
  app.run(debug=True)
