(function () {
    window.onload = init;

    var startButton;
    var counter = 0;
    var startLatitude = null;
    var startLongitude = null;
    var currentLatitude = null;
    var currentLongitude = null;
    var journeyLatitude = [];
    var journeyLongitude = [];

    // register the event handlers

    function init() {
        startButton = document.getElementById("startButton");
        startButton.onclick = getLocation;
    }

    // gets current position
    function getLocation() {
        navigator.geolocation.getCurrentPosition(startTrackingLocation);
    }

    // starts tracking the bird
    function startTrackingLocation(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;

        if (counter == 0) {
            // sets initial variables before tracking
            startLatitude = latitude;
            startLongitude = longitude;

            currentLatitude = latitude;
            currentLongitude = longitude;

            journeyLatitude.push(latitude);
            journeyLongitude.push(longitude);
        }

        counter++; // increments the update text on html

        document.getElementById("startButton").disabled = true; // disables button after program starts

        if (counter > 0) {
            // updates location
            updateMyLocation();
        }
        showOnMap(); // shows the markers

        // updates text on html
        document.getElementById("counter").innerHTML = "Update#: " + counter;
        document.getElementById("latitude").innerHTML = "Start Latitude: " + startLatitude;
        document.getElementById("longitude").innerHTML = "Start Longitude: " + startLongitude;
        document.getElementById("currentLatitude").innerHTML = "Current Latitude: " + currentLatitude;
        document.getElementById("currentLongitude").innerHTML = "Current Longitude: " + currentLongitude;
    }

    // updates location
    function updateMyLocation() {
        if (counter > 0) {
            // sets timeout to 5 secs
            setTimeout(getLocation, 5000);
        }

        if (counter > 1) {
            // randomizes position
            currentLatitude = currentLatitude + Math.random() / 100;
            currentLongitude = currentLongitude - Math.random() / 100;

            // add the journey path to list
            journeyLatitude.push(currentLatitude);
            journeyLongitude.push(currentLongitude);
        }
    }

    // show marker and lines
    function showOnMap() {
        var startPosition = new google.maps.LatLng(startLatitude, startLongitude);
        var currentPosition = new google.maps.LatLng(currentLatitude, currentLongitude);

        var mapOptions = {
            zoom: 12.5,
            center: currentPosition,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        };

        map = new google.maps.Map(document.getElementById("map"), mapOptions);

        var startMarker = new google.maps.Marker({
            position: startPosition,
        });

        var currentMarker = new google.maps.Marker({
            position: currentPosition,
        });

        startMarker.setMap(map);
        currentMarker.setMap(map);

        // sets the lines from start position to current position
        if (counter > 1) {
            for (let i = 0; i < journeyLatitude.length - 1; i++) {
                var myLine = new google.maps.Polyline({
                    path: [new google.maps.LatLng(journeyLatitude[i], journeyLongitude[i]), new google.maps.LatLng(journeyLatitude[i + 1], journeyLongitude[i + 1])],
                    strokeColor: "#0000FF",
                    strokeWeight: 3,
                });
                myLine.setMap(map);
            }
        }
    }
})();
