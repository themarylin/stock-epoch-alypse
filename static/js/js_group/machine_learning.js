// this script creates a stock chart with event-markers for DIS stock.
var date = [];
var price = [];

//this is the first chart that shows a comparison of states
d3.json("/api?stock=DIS").then(function (response) {
    jump = 200;
    stocks = response.data;
    for (var i = 0; i < stocks.length / jump; i++) {
        for (var j = 0; j < jump; j++) {
            var count = i * jump + j;
            date.push(stocks[count].date);
            price.push(stocks[count].price);
        }
    };
    renderLineChart(date, price, 'DIS_results');

});

function renderLineChart(x_values, y1, chartname) {
    var trace1 = {
        x: x_values,
        y: y1,
        name: 'Total Positions',
        mode: 'lines',
        line: {
            color: '#17BECF'
        }
    };

    var data = [trace1];

    var layout = {
        autosize: true,
        title: 'Machine Learning DIS Prediction Results:',
        height: 500,
        annotations: [{
            x: "1970-01-13",
            y: 0.541131657,
            xref: 'x',
            yref: 'y',
            text: 'IPO Date',
            showarrow: true,
            arrowhead: 7,
            ax: 0,
            ay: -40
        }]
    };

    Plotly.newPlot(chartname, data, layout);
};