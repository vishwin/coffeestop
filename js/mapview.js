var map;

// Ready function
$(document).ready(function() {

	map  = new google.maps.Map(document.getElementById('map'), {
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		zoom: 15
	}); 

});