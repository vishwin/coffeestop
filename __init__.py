#!/usr/bin/python2.7
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

app=Flask(__name__)
app.config.from_object('config')

import views
