from flask import render_template
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github')
def github():
    name = "tmax818"
    endpoint = f"https://api.github.com/users/{name}"
    res = requests.get(endpoint)
    return res.json()

