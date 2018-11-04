//this calls the button function and extracts values based on user input
$(document).ready(function () {
    $('#ml_button').on('click', values = json_url);
});

function json_url() {

    var dates1 = [];
    var pred1 = [];
    var his1 = [];
    var url;

    var values = [];
    var epoch = ($("#epoch_dropdown").val());
    var learnrate = ($("#learnrate_dropdown").val());
    var stock = ($("#stock_dropdown").val());

    values.push(epoch);
    values.push(learnrate);
    values.push(stock);
    url = "/api/ml?stock=" + stock + "&epochs=" + epoch + "&learnrate=" + learnrate + "&split=0.75";

    d3.json(url).then(function (response) {
        jump = 50;
        stocks = response.data;
        rep = Math.floor(stocks.length / jump);
        rem = (stocks.length % jump) - 1;

        for (var i = 0; i <= (rep); i++) {
            if (i == (rep)) {
                for (var j = 0; j < rem; j++) {
                    var count = i * jump + j;
                    dates1.push(stocks[count].date);
                    pred1.push(+stocks[count].prediction.toFixed(2));
                    his1.push(+stocks[count].actual.toFixed(2));
                };
            } else {
                for (var j = 0; j < jump; j++) {
                    var count = i * jump + j;
                    dates1.push(stocks[count].date);
                    pred1.push(+stocks[count].prediction.toFixed(2));
                    his1.push(+stocks[count].actual.toFixed(2));
                };
            };
        };

        renderLineChart2(dates1, pred1, his1, 'ml_manip');
    });

};

function renderLineChart2(x_values, y1, y2, chartname) {
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
        title: 'Machine Learning Manipulator:',
        height: 500,
        width: 1200
    };

    Plotly.newPlot(chartname, data, layout);
};