#!/usr/bin/python2.7
from coffeestop import app
from flask import request, redirect, url_for, render_template
from werkzeug import secure_filename
import tempfile, os

@app.route('/')
def herro():
	return 'Coffeestop is coming soon.'

from config import ALLOWED_EXTENSIONS
app.config['UPLOAD_FOLDER']=tempfile.gettempdir()
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method=='POST':
		file=request.files['gpxupload']
		if file and allowed_file(file.filename):
			return file.read()
	else:
		return render_template('upload.html')
