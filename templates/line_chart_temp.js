<!--================ First Line Area =================-->
<div id="container"></div>
<script src="https://cdn.anychart.com/releases/8.4.0/js/anychart-base.min.js"></script>
<script src="https://cdn.anychart.com/releases/8.4.0/js/anychart-ui.min.js"></script>
<script src="https://cdn.anychart.com/releases/8.4.0/js/anychart-exports.min.js"></script>
<script src="https://cdn.anychart.com/releases/8.4.0/js/anychart-stock.min.js"></script>
<script src="https://cdn.anychart.com/releases/8.4.0/js/anychart-data-adapter.min.js"></script>
<script type="text/javascript">anychart.onDocumentReady(function () {
    // The data used in this sample can be obtained from the CDN
    // https://cdn.anychart.com/samples/stock-general-features/displaying-data-in-millisecond/data.csv
    anychart.data.loadCsvFile('https://cdn.anychart.com/samples/stock-general-features/displaying-data-in-millisecond/data.csv', function (data) {
        // create data table on loaded data
        var dataTable = anychart.data.table();
        dataTable.addData(data);

        // create stock chart
        var chart = anychart.stock();

        // set chart title
        chart.title('Crystal Fluctuations');

        // create plot on the chart
        var plot = chart.plot(0);

        // create plot series with mapped data
        plot.line(dataTable.mapAs({'value': 1})).name('Sapphire');
        plot.line(dataTable.mapAs({'value': 2})).name('Cobalt');
        plot.line(dataTable.mapAs({'value': 3})).name('Topaz');

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
});</script>
<!--================ End First Line Area =================-->