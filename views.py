#!/usr/bin/python2.7
from flask import Flask
app=Flask(__name__)

@app.route('/')
def herro():
	return 'Coffeestop is coming soon.'

if __name__=='__main__':
	app.run()
