// this script creates a stock chart with event-markers for DIS stock.
var dates = [];
var pred = [];
var his = [];

//this is the first chart that shows a comparison of states
d3.json("/api/ml?stock=DIS&epochs=1000&learnrate=0.0003&split=0.75").then(function (response) {
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

        annotations: [{
            x: "2015-06-10",
            y: 104.6,
            xref: 'x',
            yref: 'y',
            text: 'Inside Out',
            showarrow: true,
            arrowhead: 5,
            ax: 0,
            ay: -50
        },
        {
            x: "2015-08-03",
            y: 115.83,
            xref: 'x',
            yref: 'y',
            text: 'Q2 F/S Report missed Wall Street Estimates',
            showarrow: true,
            arrowhead: 5,
            ax: 0,
            ay: -50
        },
        {
            x: "2016-03-04",
            y: 94.79,
            xref: 'x',
            yref: 'y',
            text: 'Zootopia',
            showarrow: true,
            arrowhead: 5,
            ax: 0,
            ay: -100
        },
        {
            x: "2016-06-16",
            y: 94.69,
            xref: 'x',
            yref: 'y',
            text: 'Opening Shanghai Disney Resort',
            showarrow: true,
            arrowhead: 5,
            ax: 0,
            ay: -110
        },
        {
            x: "2017-05-30",
            y: 105.82,
            xref: 'x',
            yref: 'y',
            text: 'Pandora The World of AVATAR Opening',
            showarrow: true,
            arrowhead: 5,
            ax: 0,
            ay: -100
        },
        {
            x: "2017-11-22",
            y: 101.11,
            xref: 'x',
            yref: 'y',
            text: 'Coco',
            showarrow: true,
            arrowhead: 5,
            ax: 0,
            ay: -70
        },
        {
            x: "2018-07-02",
            y: 104.49,
            xref: 'x',
            yref: 'y',
            text: 'Toy Story Land Opening',
            showarrow: true,
            arrowhead: 5,
            ax: 0,
            ay: -70
        }
    
    ]
    };

    Plotly.newPlot(chartname, data, layout);
};