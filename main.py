from flask import Flask, url_for, request

from flask_cors import CORS
from models.chat import Chat
from models.base import telegram_db



from models.user import User

app = Flask(__name__)

from auth.view import *
from chat.view import *

# @app.errorhandler()
# def handle_exception(e):
#   print(e)


CORS(app)
# @app.after_request
# def add_header(response):
#     return response

if __name__ == "__main__":
    telegram_db.drop_tables([User, Chat])
    telegram_db.create_tables([User, Chat])
    app.run(debug=True)
