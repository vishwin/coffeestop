#!/usr/bin/python2.7
from coffeestop import app

@app.route('/')
def herro():
	return 'Coffeestop is coming soon.'
