// Get the Roadster endpoint
const url = "http://127.0.0.1:5000/api/v1.0/mass-graph"

// Fetch the JSON data and console log it
d3.json(url).then(function(data) {
console.log(data);


let trace1 = {
    x: data.mass,
    y: data.class,
    type: 'bar',
    orientation : 'h'
  };

  let data1 = [trace1];

  // Pass metric to chart title
  let layout = {
    title: `Meteorite`
  };

  Plotly.newPlot("plot", data1, layout);



});




  // Invoke the plot creating function
  


