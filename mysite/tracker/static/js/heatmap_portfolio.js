/**
 * Created by Rivka on 20/03/2017.
 */

var config = {
  container: document.getElementById('heatmapContainer'),
  radius: 40,
  maxOpacity: .5,
  minOpacity: 0,
  blur: .75
};
var heatmapInstance = h337.create(config);



function newfunct(info) {
    var coordinates = JSON.parse(info);
    for (i = 0; i < coordinates.length; i++) {
        if (Object.values(coordinates[i])[2] === "/tracker/portfolio/") {
            console.log(Object.values(coordinates[i])[1]);
            coordinates[i].value = 100;
            var dataPoint = {
            x: Object.values(coordinates[i])[0], // x coordinate of the datapoint, a number
            y: Object.values(coordinates[i])[1], // y coordinate of the datapoint, a number
            value: Object.values(coordinates[i])[2] // the value at datapoint(x, y)
            };
            heatmapInstance.addData(dataPoint);
        }
    }
}


var request = new XMLHttpRequest();
request.open('GET', 'http://127.0.0.1:8000/tracker/api/index/3/', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    var resp = request.responseText;
    console.log(resp);
    newfunct(resp);
  } else {
    console.log("We reached our target server, but it returned an error");

  }
};

request.onerror = function() {
  console.log("There was a connection error of some sort")
};

request.send();

