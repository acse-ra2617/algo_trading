# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:28:22 2021

@author: acse-ra2617
"""

# main library website: https://flask.palletsprojects.com/en/1.1.x/
# guickstart documentation:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    title = 'CoinView'
    return render_template('index.html', title=title)


@app.route('/buy')
def buy():
    return 'buy'


@app.route('/sell')
def sell():
    return 'sell'


@app.route('/settings')
def settings():
    return 'settings'
