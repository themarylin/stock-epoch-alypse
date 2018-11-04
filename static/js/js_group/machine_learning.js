// this script creates a stock chart with event-markers for DIS stock.
var dates = [];
var pred = [];
var his = [];

//this is the first chart that shows a comparison of states
d3.json("/api/ml?stock=DIS&epochs=1000&learnrate=0.003&split=0.8").then(function (response) {
    jump = 50;
    stocks = response.data;
    rep = Math.floor(stocks.length / jump);
    rem = (stocks.length % jump) - 1;

    for (var i = 0; i <= (rep); i++) {
        if (i == (rep)) {
            for (var j = 0; j < rem; j++) {
                var count = i * jump + j;
                dates.push(stocks[count].date);
                pred.push(+stocks[count].prediction.toFixed(2));
                his.push(+stocks[count].actual.toFixed(2));
            };
        } else {
            for (var j = 0; j < jump; j++) {
                var count = i * jump + j;
                dates.push(stocks[count].date);
                pred.push(+stocks[count].prediction.toFixed(2));
                his.push(+stocks[count].actual.toFixed(2));
            };
        };
    };
    
    renderLineChart(dates, pred, his, 'DIS_results');

});

function renderLineChart(x_values, y1, y2, chartname) {
    var trace1 = {
        x: x_values,
        y: y1,
        name: 'Prediction',
        mode: 'lines',
        line: {
            color: '#17BECF'
        }
    };
    var trace2 = {
        x: x_values,
        y: y2,
        name: 'Historical',
        mode: 'lines'
    };

    var data = [trace1, trace2];

    var layout = {
        autosize: true,
        title: 'Machine Learning DIS Prediction Results:',
        height: 500,

        //Event Markers - indicating large unprecedented price changes

        // annotations: [{
        //     x: "1970-01-13",
        //     y: 0.541131657,
        //     xref: 'x',
        //     yref: 'y',
        //     text: 'IPO Date',
        //     showarrow: true,
        //     arrowhead: 7,
        //     ax: 0,
        //     ay: -40
        // },
        // {
        //     x: "1964-01-27",
        //     y: 0.149277699,
        //     xref: 'x',
        //     yref: 'y',
        //     text: 'IPO Date',
        //     showarrow: true,
        //     arrowhead: 7,
        //     ax: 0,
        //     ay: -40
        // }]
    };

    Plotly.newPlot(chartname, data, layout);
};