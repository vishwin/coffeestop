#!/usr/bin/python2.7
from flask import Flask

app=Flask(__name__)
app.config.from_object('config')

import views
