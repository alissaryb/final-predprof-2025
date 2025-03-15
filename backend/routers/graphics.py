import flask
import sqlalchemy
from flask import render_template

from .dependency_injection import inject_session


blueprint = flask.Blueprint(
    'graphics_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/cards', methods=['GET', 'POST'])
@inject_session()
def cards(session: sqlalchemy.orm.Session):
    return render_template('cards.html')


@blueprint.route('/tablo', methods=['GET', 'POST'])
@inject_session()
def tablo(session: sqlalchemy.orm.Session):
    return render_template('tablo.html')


@blueprint.route('/graph_circular', methods=['GET', 'POST'])
@inject_session()
def graph_circular(session: sqlalchemy.orm.Session):
    return render_template('graph_circular.html')


@blueprint.route('/graph_linear', methods=['GET', 'POST'])
@inject_session()
def graph_linear(session: sqlalchemy.orm.Session):
    return render_template('graph_linear.html')
