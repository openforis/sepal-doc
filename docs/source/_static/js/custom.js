function init() {
  var map = L.map("map", { zoomControl: false }).setView([0, 0], 3);

  //CartoDB layer names: light_all / dark_all / light_nonames / dark_nonames
  var layers = {
    light: L.tileLayer(
      "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png",
      { attribution: "" }
    ),
    dark: L.tileLayer(
      "https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png",
      { attribution: "" }
    ),
  };

  const startTheme = document.documentElement.dataset.theme
    ? document.documentElement.dataset.theme
    : "light";
  layers[startTheme].addTo(map);

  // Don't show the 'Powered by Leaflet' text. Attribution overload
  map.attributionControl.setPrefix("");

  // Remove all interaction
  map.dragging.disable();
  map.touchZoom.disable();
  map.doubleClickZoom.disable();
  map.scrollWheelZoom.disable();
  map.boxZoom.disable();
  map.keyboard.disable();
  if (map.tap) map.tap.disable();
  document.getElementById("map").style.cursor = "default";

  // observe html theme value
  const mutationCallback = (mutationsList) => {
    for (const mutation of mutationsList) {
      // exit if not the correct attribute
      if (
        mutation.type !== "attributes" ||
        mutation.attributeName == "data-theme"
      ) {
        return;
      }

      // refactor the map
      var theme = mutation.target.getAttribute("data-theme");

      //alert(map.hasLayer(layers[theme]));

      if (!map.hasLayer(layers[theme])) {
        // remove the layers
        map.eachLayer(function (layer) {
          map.removeLayer(layer);
        });

        // add the correct one
        layers[theme].addTo(map);
      }
    }
  };

  const observer = new MutationObserver(mutationCallback);
  observer.observe(document.documentElement, { attributes: true });
}

window.onload = init;
