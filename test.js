if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position) {
        console.log("Latitude: " + position.coords.latitude);
        console.log("Longitude: " + position.coords.longitude);
    });
} else {
    console.log("Geolocation is not available in this browser.");
}
