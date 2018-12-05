var dates = [];
var dates_rand = [];
var ideal = [];
var snp = [];
var random = [];
var ml = []

//render charts for all 4 scenarios
d3.json("api/rand").then(function (rand_response) {
    var jump1 = 50;
    var stocks1 = rand_response[0].data;
    var rep1 = Math.floor(stocks1.length / jump1);
    var rem1 = (stocks1.length % jump1) - 1;
    var random_perc = (stocks1[stocks1.length - 1].adj_comp_earning)*100;
    console.log(random_perc);
    if (random_perc < 0){
        random_perc = 0;
    };
    var a = document.getElementById("random_percent");
    a.setAttribute("dpercentage", random_perc.toFixed(0));

    for (var i = 0; i <= (rep1); i++) {
        if (i == (rep1)) {
            for (var j = 0; j < rem1; j++) {
                var count1 = i * jump1 + j;
                dates_rand.push(stocks1[count1].date);
                random.push(+(stocks1[count1].adj_comp_earning).toFixed(2));
            };
        } else {
            for (var j = 0; j < jump1; j++) {
                var count1 = i * jump1 + j;
                dates_rand.push(stocks1[count1].date);
                random.push(+(stocks1[count1].adj_comp_earning).toFixed(2));
            };
        }
    };

    var ticker = rand_response[0].stock;
    var name = 'Random (' + ticker + ')';

    renderLineChart(dates_rand, random, 'random-chart', name);
});

d3.json("api/scen").then(function (response) {
    var jump = 50;
    var stocks = response.data;
    var rep = Math.floor(stocks.length / jump);
    var rem = (stocks.length % jump) - 1;

    for (var i = 0; i <= (rep); i++) {
        if (i == (rep)) {
            for (var j = 0; j < rem; j++) {
                var count = i * jump + j;
                dates.push(stocks[count].date);
                ideal.push(+(stocks[count].ideal_earning).toFixed(2));
                snp.push(+(stocks[count].snp_500).toFixed(2));
                ml.push(+(stocks[count].ml).toFixed(2));
            };
        } else {
            for (var j = 0; j < jump; j++) {
                var count = i * jump + j;
                dates.push(stocks[count].date);
                ideal.push(+(stocks[count].ideal_earning).toFixed(2));
                snp.push(+(stocks[count].snp_500).toFixed(2));
                ml.push(+(stocks[count].ml).toFixed(2));
            };
        }
    };
    renderLineChart(dates, ideal, 'ideal-chart', 'Ideal (DIS)');
    renderLineChart(dates, ml, 'ml-chart', 'Machine-Learning (DIS)');
    renderLineChart(dates, snp, 'snp500-chart', 'Buy & Hold (S&P 500)');
})

//this builds the bar chart for the first half of html
function renderLineChart(x_values, y1, chartname, name) {
    if (chartname == 'snp500-chart') {
        line_color = '#000000';
    } else {
        line_color = '#17BECF';
    };
    var trace1 = {
        x: x_values,
        y: y1,
        text: y1,
        mode: 'lines',
        line: {
            color: line_color
        }
    };

    var data = [trace1];

    var layout = {
        autosize: true,
        title: 'Earnings: ' + name,
        height: 350,
        yaxis: {
            tickformat: ',.0%'
        }
    };

    Plotly.newPlot(chartname, data, layout);
};