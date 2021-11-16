from main import app
from flask.helpers import url_for


@app.route('/chts', methods=['GET'])
def get_all_chats():
  print(url_for('chats'))
  
  