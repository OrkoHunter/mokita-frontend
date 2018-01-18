# -*- coding: utf-8 -*-
import request
from flask import Flask, render_template
from flask_session import Session


APP_SECRET_KEY = 'blockchain'
APP_CONFIG_SESSION_TYPE = 'filesystem'
APP_DEBUG = True

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
app.config['SESSION_TYPE'] = APP_CONFIG_SESSION_TYPE
app.debug = APP_DEBUG

sess = Session()

# https://pythonspot.com/login-authentication-with-flask/


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        sess['logged_in'] = True
    else:
        print('wrong password!')
    return main()


@app.route("/logout")
def logout():
    sess['logged_in'] = False
    return main()


@app.route("/")
def main():
    if sess['logged_in']:
        return render_template('home.html')
    else:
        return render_template('main.html')



app.run(host='0.0.0.0', port=8080)
