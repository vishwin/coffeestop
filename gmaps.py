#!/usr/bin/python2.7
import gpxpy.parser as parser

class Map:
	def __init__(self, gpxstring):
		self.gpx=parser.GPXParser(gpxstring).parse()
	
	def genjs(self):
		self.js="""\
function initialize() {
	var mapOptions={
		mapTypeId: google.maps.MapTypeId.TERRAIN
	};
	
	var map=new google.maps.Map(document.getElementById('map'), mapOptions);
	
	var trackCoordinates=[
"""
		for track in self.gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					self.js=self.js+"""\
		new google.maps.LatLng({0}, {1}),
""".format(point.latitude, point.longitude)
		self.js=self.js+"""\
	];
	var track=new google.maps.Polyline({
		path: trackCoordinates,
		geodesic: true,
		strokeColor: '#FF0000',
		strokeOpacity: 1.0,
		strokeWeight: 2
	});
	
	track.setMap(map);
}

google.maps.event.addDomListener(window, 'load', initialize);
"""
		return self.js
