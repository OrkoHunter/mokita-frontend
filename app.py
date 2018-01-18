# -*- coding: utf-8 -*-
from flask import Flask, render_template


APP_SECRET_KEY = 'blockchain'
APP_CONFIG_SESSION_TYPE = 'filesystem'
APP_DEBUG = True

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
app.config['SESSION_TYPE'] = APP_CONFIG_SESSION_TYPE
app.debug = APP_DEBUG


@app.route("/")
def main():
    return render_template('main.html')

app.run(host='0.0.0.0', port=8080)
