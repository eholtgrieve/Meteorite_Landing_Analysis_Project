//Year Graph
//Get the Roadster endpoint
const url = "http://127.0.0.1:5000/api/v1.0/yearly-graph"
// const url = "/api/v1.0/yearly-graph"

//Fetch the JSON data and console log it
d3.json(url).then(function(data) {
console.log(data);

  let values = Object.values(data);
  
    let trace = {
      x: Object.keys(data),
      y: values,
      mode: 'lines'
    }

    let data1 = [trace];

    // Pass metric to chart title
    let layout = {
      xaxis: {range: [1980, 2015], title: "Year"},
      yaxis: {range: [0, 3000], title: "Count"},
      title: `Yearly Counts of Meteorites Fallen between 1980 and 2013`
    };

  Plotly.newPlot("plot", data1, layout);


});

  


