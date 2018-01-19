# -*- coding: utf-8 -*-
import requests
from flask import Flask, render_template, session
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
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        print('wrong password!')
    return main()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return main()


@app.route("/")
def main():
    if session.get('logged_in', False):
        return render_template('home.html')
    else:
        return render_template('main.html')


app.run(host='0.0.0.0', port=8081)

'''
 - Blockchain event
    - http://localhost:8080/
    - https://github.com/creativetimofficial/light-bootstrap-dashboard
    - https://www.mykgp.com/
'''
