from flask import Flask, render_template, redirect, url_for, request
import requests
from random import choice

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="")


@app.route('/cards', methods=['GET', 'POST'])
def cards():
    return render_template('cards.html')


@app.route('/tablo', methods=['GET', 'POST'])
def tablo():
    return render_template('tablo.html')


@app.route('/graph_circular', methods=['GET', 'POST'])
def graph_circular():
    return render_template('graph_circular.html')


@app.route('/graph_linear', methods=['GET', 'POST'])
def graph_linear():
    return render_template('graph_linear.html')


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1', threaded=True)
