#!/usr/bin/python2.7
import gpxpy.parser
import json
import sys
import urllib
import urllib2
import oauth2
from config import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

class Yelp:
	def __init__(self, consumer_key, consumer_secret, token, token_secret, gpxstring):
		self.consumer_key=consumer_key
		self.consumer_secret=consumer_secret
		self.token=token
		self.token_secret=token_secret
		self.gpx=gpxpy.parser.GPXParser(gpxstring).parse()
	
	def query(self, lat, lon):
		url_params={
			'category_filter': 'food',
			'radius_filter': 2000, # 2 km on either side of route
			'll': '{0},{1}'.format(lat, lon)
		}
		encoded_params=urllib.urlencode(url_params)
		url='http://api.yelp.com/v2/search/?' + encoded_params
		
		consumer=oauth2.Consumer(self.consumer_key, self.consumer_secret)
		oauth_request=oauth2.Request('GET', url, {})
		oauth_request.update(
			{
				'oauth_nonce': oauth2.generate_nonce(),
				'oauth_timestamp': oauth2.generate_timestamp(),
				'oauth_token': self.token,
				'oauth_consumer_key': self.consumer_key
			}
		)
		token=oauth2.Token(self.token, self.token_secret)
		oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
		signed_url=oauth_request.to_url()
		
		connection=urllib2.urlopen(signed_url, None)
		try:
			response=json.loads(connection.read())
		finally:
			connection.close()
		
		return response
	
	def query_all_cleaned(self):
		places=[]
		for track in self.gpx.tracks:
			for segment in track.segments:
				for place in self.query(lat=segment.points[0].latitude, lon=segment.points[0].longitude)['businesses']:
					places.append(place)
		for k, g in itertools.groupby(places, lambda x: x['id']):
			places=g.next()
		return places
