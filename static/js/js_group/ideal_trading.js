function drawLineChart() {

    // Add a helper to format timestamp data
    // Date.prototype.formatMMDDYYYY = function() {
    //     return (this.getMonth() + 1) +
    //     "/" +  this.getDate() +
    //     "/" +  this.getFullYear();
    // }
    var date = [];
    var compound_earning = [];
    
    //this is the first chart that shows a comparison of states
    // <script src="{{url_for('static', filename='js/js_group/machine_learning.js')}}"></script>
    <script src="js/js_group/machine_learning.js"></script>
    d3.json("{{url_for('data', filename='ideal_trading_scenario.json')}}").then(function (response) {
    //d3.json("{{url_for('data', filename='ideal_trading_scenario.json')}}").then(function (response) {    
        response.forEach(function (d) {
            date.push(d.date);
            compound_earning.push(d.compound_earning);
        });

    })    
  
      // Create the chart.js data structure using 'date' and 'compound_earning'
      var tempData = {
        labels : date,
        datasets : [{
            fillColor             : "rgba(151,187,205,0.2)",
            strokeColor           : "rgba(151,187,205,1)",
            pointColor            : "rgba(151,187,205,1)",
            pointStrokeColor      : "#fff",
            pointHighlightFill    : "#fff",
            pointHighlightStroke  : "rgba(151,187,205,1)",
            data                  : compound_earning,
        }]
      };
  
      // Get the context of the canvas element we want to select
      var ctx = document.getElementById("ideal-chart").getContext("2d");
  
      // Instantiate a new chart
      var myLineChart = new Chart(ctx).Line(tempData);
    });
  }

// http://microbuilder.io/blog/2016/01/10/plotting-json-data-with-chart-js.html
 
 
 
//Below is an Example 

//from  https://colorlib.com/polygon/cooladmin/chart.html

// function drawLineChart(){

//   var ctx = document.getElementById("ideal-chart");
//   ctx.height = 150;
//   var myChart = new Chart( ctx, {
//       type: 'line',
//       data: {
//           labels: [ "January", "February", "March", "April", "May", "June", "July" ],
//           datasets: [
//               {
//                   label: "My First dataset",
//                   borderColor: "rgba(0,0,0,.09)",
//                   borderWidth: "1",
//                   backgroundColor: "rgba(0,0,0,.07)",
//                   data: [ 22, 44, 67, 43, 76, 45, 12 ]
//                           },
//               {
//                   label: "My Second dataset",
//                   borderColor: "rgba(0, 123, 255, 0.9)",
//                   borderWidth: "1",
//                   backgroundColor: "rgba(0, 123, 255, 0.5)",
//                   pointHighlightStroke: "rgba(26,179,148,1)",
//                   data: [ 16, 32, 18, 26, 42, 33, 44 ]
//                           }
//                       ]
//       },
//       options: {
//           responsive: true,
//           tooltips: {
//               mode: 'index',
//               intersect: false
//           },
//           hover: {
//               mode: 'nearest',
//               intersect: true
//           }

//       }
//   } );

// }
