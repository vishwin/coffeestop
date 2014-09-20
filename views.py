#!/usr/bin/python2.7
from coffeestop import app
from flask import request, redirect, render_template, session, flash

@app.route('/')
def herro():
	return 'Coffeestop is coming soon.'

from config import ALLOWED_EXTENSIONS
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method=='POST':
		file=request.files['gpxupload']
		if file and allowed_file(file.filename):
			session['gpxfile']=file.read()
			return 'GPX successfully uploaded. More to come'
		else:
			flash('Improper file or file is larger than 1&nbsp;MiB.')
		return render_template('upload.html')
