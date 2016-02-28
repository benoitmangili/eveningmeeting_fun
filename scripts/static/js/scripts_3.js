var main = function() {
  // insert code here
  $("#temperatureBtn").click(function() {
      $.ajax({
              url: "/temperature",
              type: "get",
      }).done(function (data) {
        $( "#current_temperature" ).text( data.value.toFixed(2) + "°C" );
        $( "#graphBtn" ).show();
      });
  });



  $("#graphBtn").click(function() {

    $('#graphdiv').show();
    setInterval(function() {
      $.ajax({
              url: "/temperature",
              type: "get",
      }).done(function (data) {
        if (temps.push(data) > 10 ) temps.shift()
        plot(temps)
      });
    }, 1000);
    $("#graphBtn" ).hide();
    $("#graphBtn").off('click')
  });
};

$("#graphBtn" ).hide();
$('#graphdiv').hide();





var svg = d3.select('#graph')
  .append('div')
  .attr('class', 'svg-container')
  .append('svg')
  .attr("preserveAspectRatio", "xMinYMin meet")   
  .attr("viewBox", "0 0 400 400")
   //class to make it responsive
  .attr('class', "svg-content-responsive", true);

var temps = [];

svg.append('line')
  .attr('class', 'axis')
  .attr('x1', 30)
  .attr('y1', 20)
  .attr('x2', 30)
  .attr('y2', 271);

svg.append('line')
  .attr('class', 'axis')
  .attr('x1', 29)
  .attr('y1', 270)
  .attr('x2', 390)
  .attr('y2', 270)

svg.append('text')
  .attr('class', 'legend')
  .attr('x', 10)
  .attr('y', 25)
  .attr('font-size', 14)
  .text('25')

svg.append('text')
  .attr('class', 'legend')
  .attr('x', 10)
  .attr('y', 275)
  .attr('font-size', 14)
  .text('15')




var ymin = 60;
var w = (390 - 50) / 10 - 2 ;

function plot(data) {
  var bar = svg.selectAll('.bar')
                .data(data)
  bar
    .enter()
    .append('rect')
    .attr('class', 'bar')
    .attr('x', function(d,i){ return (w + 2)*i + 40 })
    .attr('width', w )
    .attr('y', 0)

  bar
    .attr('y', function(d,i){
      var y = 269 - 10 * d.value;
      console.log(y)
      return y;
     })
    .attr('height', function(d,i){
      var y = 10 * d.value;
      console.log(y)
      return y;
     })


}


$(document).ready(main);


