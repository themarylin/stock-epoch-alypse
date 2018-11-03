var date = [];
var ideal = [];
var snp = [];

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

d3.json("api/scen").then(function (response){
    jump = 18;
    stocks = response.data;
    for (var i = 0; i < stocks.length/jump; i++){
        for (var j = 0; j < jump; j++){
            var count = i*jump+j;
            date.push(stocks[count].date);
            ideal.push(stocks[count].ideal_earning);
            snp.push(stocks[count].snp_500);
        }
    };
    
    renderLineChart(date, ideal, 'ideal-chart', 'Ideal');
    renderLineChart(date, ideal, 'random-chart', 'Random');
    renderLineChart(date, ideal, 'ml-chart', 'Machine-Learning');
    renderLineChart(date, snp, 'snp500-chart', 'S&P 500');
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