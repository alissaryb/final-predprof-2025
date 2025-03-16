import os
from os import abort

import requests
from dotenv import load_dotenv
from flask import Flask, render_template
from werkzeug.utils import redirect

from backend.forms.url import FormUrl

from backend.database import db_session
from backend.routers import graphics, users
from backend.routers.users import index

app = Flask(__name__)


@app.route("/change_url", methods=['POST'])
def change_url():
    form = FormUrl()
    if form.validate_on_submit():
        url = form.url
        try:
            req = requests.get(url)
        except Exception:
            abort(400)
        with open("backend/src/url_addr.txt") as f:
            f.write(url)
    return redirect("/")


if __name__ == "__main__":
    db_session.init()
    app.register_blueprint(graphics.blueprint)
    app.register_blueprint(users.blueprint)

    load_dotenv()
    app.run(port=int(os.getenv('SERVER_PORT', 8080)), host=os.getenv('SERVER_HOST', '127.0.0.1'), threaded=True)
