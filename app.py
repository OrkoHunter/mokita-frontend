# -*- coding: utf-8 -*-
import hashlib
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
    url = "http://localhost:3000/api/Identity_u/{}${}".format(username, password)
    r = requests.get(url)
    if r.status_code == 200:
        session['logged_in'] = True
    else:
        print('Wrong password!')
    return main()


@app.route('/signup', methods=['POST'])
def do_admin_signup():
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    type_of_user = request.form['type_of_user']
    email = request.form['email']
    dollar_class = 'org.acme.biznet.Identity_u'

    h = hashlib.sha1()
    h.update(password.encode('utf-8'))
    idenID = username + '$' + h.hexdigest()

    url = "http://localhost:3000/api/Identity_u"
    data = {
        'idenId': idenID,
        'name': name,
        'type': type_of_user,
        'email': email,
        '$class': 'org.acme.biznet.Identity_u'
    }
    import os
    os.environ['NO_PROXY'] = 'localhost'
    headers = {'content-type': 'application/json'}
    print (data)
    import json
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print (r)
    if r.status_code == 200:
        session['logged_in'] = True
    return main()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return main()


@app.route("/")
def main():
    # return render_template("dashboard.html")
    if session.get('logged_in', False):
        print ('sgjbjsdbvjsdbvj')
        return render_template('dashboard.html')
    else:
        print ('skdjbv')
        return render_template('main.html')


@app.route("/create")
def create():
    return render_template("create-track.html")

app.run(host='0.0.0.0', port=8081)
