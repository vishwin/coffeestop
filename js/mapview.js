var map;

// Ready function
$(document).ready(function() {

    var pyrmont = new google.maps.LatLng(-33.8665433,151.1956316);

	map  = new google.maps.Map(document.getElementById('map'), {
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		center: pyrmont,
		zoom: 15
	}); 

});