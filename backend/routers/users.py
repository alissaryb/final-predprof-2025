import flask
import sqlalchemy
from flask import render_template

from .dependency_injection import inject_session


blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/', methods=['GET', 'POST'])
@inject_session()
def index(session: sqlalchemy.orm.Session):
    return render_template("index.html", title="")
