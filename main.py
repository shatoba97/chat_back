from flask import Flask, url_for, request
from peewee import *
from flask_cors import CORS

telegram_db = SqliteDatabase("telegram.db")

app = Flask(__name__)

from auth.view import *

# @app.errorhandler()
# def handle_exception(e):
#   print(e)


@app.after_request
def add_header(response):
    return response

CORS(app)
if __name__ == "__main__":
    app.run(debug=True)
