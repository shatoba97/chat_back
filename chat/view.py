from main import app
from flask.helpers import url_for

from service.token_required import token_req


@app.route("/chats", methods=["GET"])
@token_req
def get_all_chats(e):
    print(url_for("chats"), e)
