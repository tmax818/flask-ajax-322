from flask import render_template, jsonify
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github')
def github():
    res = {"user_name":"tmax818"}
    
    return jsonify(res)

