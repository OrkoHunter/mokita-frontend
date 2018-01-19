# -*- coding: utf-8 -*-
import requests
from flask import Flask, render_template, session, request
# from flask_session import Session


APP_SECRET_KEY = 'blockchain'
APP_CONFIG_SESSION_TYPE = 'filesystem'
APP_DEBUG = True

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
app.config['SESSION_TYPE'] = APP_CONFIG_SESSION_TYPE
app.debug = APP_DEBUG

# https://pythonspot.com/login-authentication-with-flask/


@app.route('/login', methods=['POST'])
def do_admin_login():
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    url = "http://localhost:3000/api/Identity_u/{}${}".format(username, password)
    r = requests.get(url)
    if r.status_code == 200:
        session['logged_in'] = True
    else:
        print('Wrong password!')
    return main()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return main()


@app.route("/")
def main():
    # return render_template("dashboard.html")
    if session.get('logged_in', False):
        return render_template('dashboard.html')
    else:
        return render_template('main.html')


@app.route("/create")
def create():
    return render_template("create-track.html")

app.run(host='0.0.0.0', port=8081)
