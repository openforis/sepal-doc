function init() {
    var map = L.map('map', { zoomControl: false }).setView([0, 0], 3);
        
    //CartoDB layer names: light_all / dark_all / light_nonames / dark_nonames
    var layer = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
        });
        
    layer.addTo(map);
    map.attributionControl.setPrefix(''); // Don't show the 'Powered by Leaflet' text. Attribution overload

    // Remove all interaction
    map.dragging.disable();
    map.touchZoom.disable();
    map.doubleClickZoom.disable();
    map.scrollWheelZoom.disable();
    map.boxZoom.disable();
    map.keyboard.disable();
    if (map.tap) map.tap.disable();
    document.getElementById('map').style.cursor='default';
};

window.onload = init;