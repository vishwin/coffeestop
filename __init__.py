#!/usr/bin/python2.7
from flask import Flask, session
import os

app=Flask(__name__)
app.config.from_object('config')

app.secret_key=os.urandom(24)

import views
