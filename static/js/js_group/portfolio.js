var date = [];
var price = [];

//this is the first chart that shows a comparison of states
d3.json("api?stock=DIS").then(function (response) {
    response.data.forEach(function (d) {
        date.push(d.date);
        price.push(d.price);
        renderLineChart(date, price, 'ideal-chart', 'Ideal');
        renderLineChart(date, price, 'random-chart', 'Random');
        renderLineChart(date, price, 'ml-chart', 'Machine-Learning');
        renderLineChart(date, price, 'snp500-chart', 'S&P 500');
    });

})

//this builds the bar chart for the first half of html
function renderLineChart(x_values, y1, chartname, name) {
    var trace1 = {
        x: x_values,
        y: y1,
        text: y1,
        name: 'Total Positions',
        mode: 'lines',
        textposition: 'auto',
        hoverinfo: 'none'
    };

    var data = [trace1];

    var layout = {
        autosize: true,
        title: 'DIS Earnings:'+name,
        height:350,           
    };

    Plotly.newPlot(chartname, data, layout);
};