var dates = [];
var ideal = [];
var snp = [];
var random = [];
var ml = []

//this is the first chart that shows a comparison of states


// d3.json("api?stock=DIS").then(function (response) {
//     response.data.forEach(function (d) {
//         date.push(d.date);
//         price.push(d.price);
//         renderLineChart(date, price, 'ideal-chart', 'Ideal');
//         renderLineChart(date, price, 'random-chart', 'Random');
//         renderLineChart(date, price, 'ml-chart', 'Machine-Learning');
//         renderLineChart(date, price, 'snp500-chart', 'S&P 500');
//     });

// })

d3.json("api/scen").then(function (response) {
    jump = 50;
    stocks = response.data;
    rep = Math.floor(stocks.length / jump);
    rem = (stocks.length % jump) - 1;

    console.log(stocks.length);
    console.log(rep);
    console.log(rem);

    for (var i = 0; i <= (rep); i++) {
        if (i == (rep)) {
            for (var j = 0; j < rem; j++) {
                var count = i * jump + j;
                dates.push(stocks[count].date);
                ideal.push(+(stocks[count].ideal_earning*100).toFixed(2));
                snp.push(+(stocks[count].snp_500*100).toFixed(2));
                ml.push(+(stocks[count].ml*100).toFixed(2));
            };
        } else {
            for (var j = 0; j < jump; j++) {
                var count = i * jump + j;
                dates.push(stocks[count].date);
                ideal.push(+(stocks[count].ideal_earning*100).toFixed(2));
                snp.push(+(stocks[count].snp_500*100).toFixed(2));
                ml.push(+(stocks[count].ml*100).toFixed(2));
            };
        }
    };

    renderLineChart(dates, ideal, 'ideal-chart', 'Ideal');
    renderLineChart(dates, random, 'random-chart', 'Random');
    renderLineChart(dates, ml, 'ml-chart', 'Machine-Learning');
    renderLineChart(dates, snp, 'snp500-chart', 'S&P 500');
})

//this builds the bar chart for the first half of html
function renderLineChart(x_values, y1, chartname, name) {
    var trace1 = {
        x: x_values,
        y: y1,
        text: y1,
        mode: 'lines',
        line: {
            color: '#17BECF'
        }
    };

    var data = [trace1];

    var layout = {
        autosize: true,
        title: 'Earnings: ' + name,
        height: 350
    };

    Plotly.newPlot(chartname, data, layout);
};