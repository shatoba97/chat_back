from flask.helpers import url_for
from flask import request, jsonify, make_response
from main import app
from peewee import *
import uuid

from model import User

@app.route('/auth', methods = ["POST"])
def auth():
  print(url_for('auth'), request.json)
  auth = request.authorization
  if not auth or auth.login or auth.password:
    make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
  
  user = User.filter
  return 'request'

@app.route('/register', methods = ["POST"])
def sign_up():
  print(url_for('sign_up'))
  json = request.json
  public_id = str(uuid.uuid4())
  user = User(login = json['login'], password = json['password'], chats = list(), public_id = public_id)
  user.save()
  return dict({"token": public_id, "id": user.id})

@app.route('/get-users', methods = ["GET"])
def getUsers():
  print(url_for('auth'))
  collection = []
  query = User.select()
  for user in query:
    collection.append(dict({'login': user.login, "password": user.password, "chats": user.chats, "public_id": user.public_id}))
  return {"collection": collection}