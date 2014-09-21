#!/usr/bin/python2.7
from coffeestop import app, gmaps, yelp
from flask import request, redirect, render_template, url_for, session, flash
from config import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

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
			return redirect(url_for('map'))
		else:
			flash('Improper file or file is larger than 1&nbsp;MiB.')
	return render_template('upload.html')

@app.route('/map')
def map():
	yelpObject=yelp.Yelp(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, token=TOKEN, token_secret=TOKEN_SECRET, gpxstring=session['gpxfile'])
	
	mapObject=gmaps.Map(gpxstring=session['gpxfile'])
	mapJS=mapObject.genjs()
	
	return render_template('mapview.html', mapview=mapJS)
