// Initialize leaflet map


var map = L.map('map').setView([32.73, -17], 11.5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


// Fetch trails from your API
fetch('/api/trails')
    .then(response => response.json())
    .then(trails => {
      trails.forEach(trail => {
        if (trail.start_lat && trail.start_lon && trail.end_lat && trail.end_lon) {
        var start = [trail.start_lat, trail.start_lon];
        var end = [trail.end_lat, trail.end_lon];

        // Draw a line between start and end
        var line = L.polyline([start, end], { color: 'blue' }).addTo(map);

        // Optional: add a marker at start
        var marker = L.circleMarker(start, { radius: 4, color: 'red' }).addTo(map);

        var popupContent = `
            <strong>${trail.name}</strong><br />
            Distance: ${trail.distance_m} m<br />
            Elevation gain: ${trail.elevation_gain_m} m<br />
            Avg grade: ${trail.avg_grade} %<br />
            Strava ID: ${trail.strava_segment_id}
             `;
        line.bindPopup(popupContent);
        marker.bindPopup(popupContent);
        }
      });
    })
    .catch(err => {
       console.error('Error loading trails:', err);
    });







//var map = new L.Map('map', {
//	layers: [
//		new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//			'attribution': 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
//		})
//	],
//	center: [38.727897, -9.164737],
//	zoom: 14
// });