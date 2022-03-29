from flask import render_template, jsonify
from flask_app import app

from flask_app.models.model import Model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github')
def github():
    res = {"user_name":"tmax818"}
    
    return jsonify(res)


@app.route('/weather')
def weather():
    weather = Model.weather()
    return jsonify(weather)

