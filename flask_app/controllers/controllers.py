from flask import render_template, jsonify
from flask_app import app

from flask_app.models.model import Model

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather')
def weather():
    weather = Model.weather()
    return render_template('index.html', weather = Model.weather())

@app.route('/weather/json')
def weather_json():
    weather = Model.weather()
    return jsonify(weather)

