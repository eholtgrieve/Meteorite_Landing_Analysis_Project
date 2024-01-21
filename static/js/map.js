//creating variable for api 
let queryUrl = "http://127.0.0.1:5000/api/v1.0/landings-map";



//performing get request to query url
d3.json(queryUrl).then((data) => {
    //logging data to console to make sure its correct
    console.log(data)
    
    //creating the map object
    let myMap = L.map("map", {
        center: [45.52, -122.67],
        zoom: 5
      });
  
    //adding the tile layer
    let base = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })
    
    base.addTo(myMap);

    //creating markers
    data.forEach(result => {
        console.log(result)
        let marker = L.circleMarker([result.latitude,result.longitude], {
            color: 'black',
            fillColor: massColor(result.mass),
            fillOpacity: 0.75,
            radius: 8,
            weight: 1
        }).addTo(myMap);
        marker.bindPopup(`<h3>${result.name}</h3><hr><p>Year: ${result.year}</p><hr><p>Mass: ${result.mass} grams</p><hr><p>Class: ${result.class}</p>`);
    });


    //creating legend object
    let legend = L.control({position: "bottomleft"});
    
    //adding values to legend
    legend.onAdd = function () {
        let div = L.DomUtil.create("div", "info legend");
        let mass = [100,1000,5000,10000,50000];
        let title = ['<h3>Mass(g)</h3>'];
      
        //adding colors and labels to legend
        for (let i = 0; i < mass.length; i++) {
            title.push('<ul style="background-color:' + massColor(mass[i] + 1) + '"> <span>' + mass[i] + (mass[i + 1] ? '&ndash;' + mass[i + 1] + '' : '+') + '</span></ul>');
        }
  
        div.innerHTML += "<ul>" + title.join("") + "</ul>";
          
        return div;
      };
  
    //adding legend to map
    legend.addTo(myMap);
    
  
});

//function that changes marker color based on mass
function massColor(mass) {
    //green
    if (mass <= 100) return "#6BFF33";
    //light green
    else if (mass <= 1000) return "#D1FF33";
    //yellow green
    else if (mass <= 5000) return "#FFD433";
    //orange
    else if (mass <= 10000) return "#FFA533";
    //red orange
    else if (mass <= 50000) return "#FF7733";
    //red
    else return "#FF4233";
}

  
