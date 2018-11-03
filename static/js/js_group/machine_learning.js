// this script creates a stock chart with event-markers for DIS stock.
var date = [];
var price = [];

//this is the first chart that shows a comparison of states
d3.json("/api?stock=DIS").then(function (response) {
    response.data.forEach(function (d) {
        date.push(d.date);
        price.push(d.price);
        
        renderBarChart(date, price, 'bar_chart');
    });

})

anychart.onDocumentReady(function () {
    // The data used in this sample can be obtained from the CDN
    // https://cdn.anychart.com/samples/stock-general-features/displaying-data-in-millisecond/data.csv
    // anychart.data.loadCsvFile('https://cdn.anychart.com/samples/stock-general-features/displaying-data-in-millisecond/data.csv', function (data) {
    //     // create data table on loaded data
    //     var dataTable = anychart.data.table();
    //     dataTable.addData(data);
        
        
        var dataTable = anychart.data.table();
        // create stock chart
        var chart = anychart.stock();

        // set chart title
        chart.title('DIS Stock Price Changes');

        // create plot on the chart
        var plot = chart.plot(0);

        // create plot series with mapped data
        plot.line(price).name('Sapphire');

        // create scroller series with mapped data
        chart.scroller().line(dataTable.mapAs({'value': 1}));

        // set tooltip title formatter for the chart
        chart.tooltip().titleFormat(function () {
            return window.anychart.format.dateTime(this.hoveredDate, 'HH:mm:ss.SSS');
        });

        // set container id for the chart
        chart.container('container');
        // initiate chart drawing
        chart.draw();

        // create range picker
        var rangePicker = anychart.ui.rangePicker();
        // init range picker
        rangePicker.render(chart);

        // create range selector
        var rangeSelector = anychart.ui.rangeSelector();
        // init range selector
        rangeSelector.render(chart);
    });
});