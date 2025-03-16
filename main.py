import os
import requests
import json
from dotenv import load_dotenv
from flask import Flask, render_template, abort
from backend.database import db_session
from backend.routers import graphics, users
from backend.services.database_requests import get_stations, get_map, get_custom_map

from backend.forms.service_addresses import ServiceAddress
from backend.src.api_requests import get_all_tiles
from backend.tiles import get_field

app = Flask(__name__)
app.config['SECRET_KEY'] = "Otcheburashim"


def count_price():
    d = {}
    stations_list = get_stations()
    for i in stations_list:
        if d[i[2]] not in d:
            d[i[2]] = i[3]
        else:
            d[i[2]] += i[3]
    return d[0], d[1], d[0] + d[1]


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ServiceAddress()
    if form.validate_on_submit():
        url = form.url.data
        print(url)
        try:
            req = requests.get(url)
        except Exception:
            abort(400)
        with open('backend/src/url_addr.json', 'w') as f:
            json.dump({"url": url}, f)
        get_all_tiles()
        return render_template("index.html", form=form)
    return render_template("index.html", form=form)


@app.route('/map', methods=['GET', 'POST'])
def map():
    map = get_map()
    return render_template("map.html", map=map, len=len(map), p=count_price())

@app.route('/full', methods=['GET', 'POST'])
def full():
    map = get_custom_map(modules=True, stations=True, coverage=True)
    return render_template("full.html", map=map, len=len(map), p=count_price())

@app.route('/station', methods=['GET', 'POST'])
def station():
    map = get_custom_map(modules=False, stations=True, coverage=False)
    return render_template("station.html", map=map, len=len(map), p=count_price())

@app.route('/coverage', methods=['GET', 'POST'])
def coverage():
    map = get_custom_map(modules=False, stations=True, coverage=True)
    return render_template("coverage.html", map=map, len=len(map), p=count_price())

@app.route('/module', methods=['GET', 'POST'])
def module():
    map = get_custom_map(modules=True, stations=False, coverage=False)
    return render_template("module.html", map=map, len=len(map), p=count_price())


# print(get_field())

if __name__ == "__main__":
    db_session.init()
    app.register_blueprint(graphics.blueprint)
    app.register_blueprint(users.blueprint)

    load_dotenv()
    app.run(port=int(os.getenv('SERVER_PORT', 8080)), host=os.getenv('SERVER_HOST', '127.0.0.1'), threaded=True)
