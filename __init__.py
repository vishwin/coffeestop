#!/usr/bin/python2.7
from flask import Flask, session
from flask.ext.session import Session

app=Flask(__name__)
app.config.from_object('config')

Session(app)

import views
