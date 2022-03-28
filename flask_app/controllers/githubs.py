from flask import request, redirect, render_template, jsonify, session
from flask_app import app

from flask_app.models.github import Github

@app.route('/github_info')
def github_info():
    return render_template('github.html')


@app.route('/handle/github', methods=["POST"])
def github_form():
    print(request.form)
    res = Github.data_for_html(request.form['name'])
    session['data'] = {**res}

    return redirect('/github_info')


