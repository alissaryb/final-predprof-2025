import os

from dotenv import load_dotenv
from flask import Flask

from backend.database import db_session
from backend.routers import graphics, users


app = Flask(__name__)


if __name__ == "__main__":
    db_session.init()
    app.register_blueprint(graphics.blueprint)
    app.register_blueprint(users.blueprint)

    load_dotenv()
    app.run(port=int(os.getenv('SERVER_PORT', 8080)), host=os.getenv('SERVER_HOST', '127.0.0.1'), threaded=True)
