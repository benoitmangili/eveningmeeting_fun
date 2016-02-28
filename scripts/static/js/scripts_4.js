
var min_temp, max_temp, current_temp;
var temps = []
var graphInterval;
var controllerIsRunning;

var main = function() {
  $("#start_controller").click( start_controller  );
  $('#min_up')  .click( update_set_point_min_up   );
  $('#min_down').click( update_set_point_min_down );
  $('#max_up')  .click( update_set_point_max_up   );
  $('#max_down').click( update_set_point_max_down );
};



var start_controller = function() {
  // first, start the controller
  $.ajax({
          url: "/temperature_thread",
          type: "put",
          data: JSON.stringify({'thread_command' : 'Start'}),
          contentType: "application/json; charset=utf-8",
  })
  // then start the plot loop,
  // and get the current set_points
  .then(function (data) {

    start_plot_loop();
  
    return $.ajax({
        url:'/set_point',
        type: 'get',
      });
  })
  // update the display of the set_points
  .then( update_set_point_display )
  // show everything
  .then(function(data){
    $('#start_controller').hide();
    controllerIsRunning = true;
  })
  // if something wrong happend
  .fail(function(data){
    console.warn("???", data)
  });
}

var update_set_point = function(min_v, max_v){
  // first, update on server
  $.ajax({
    url:'/set_point',
    type: 'put',
    data: JSON.stringify({
      set_point_upper: max_v,
      set_point_lower: min_v
    }),
    contentType: "application/json; charset=utf-8",
  })
  // then update the display
  .then( update_set_point_display )
}

var update_set_point_display = function(data){
    min_temp = data['set_point_lower'];
    max_temp = data['set_point_upper'];
    $('#min_value').html(min_temp)
    $('#max_value').html(max_temp)
  }

var update_set_point_min_up   = function(){ update_set_point(min_temp+1, max_temp  ); }
var update_set_point_min_down = function(){ update_set_point(min_temp-1, max_temp  ); }
var update_set_point_max_up   = function(){ update_set_point(min_temp  , max_temp+1); }
var update_set_point_max_down = function(){ update_set_point(min_temp  , max_temp-1); }


var start_plot_loop = function() {
  if (!controllerIsRunning){
    graphInterval = setInterval(function() {
      $.ajax({
              url: "/temperature",
              type: "get",
      }).done(function (data) {
        if (temps.push(data) > 10 ) temps.shift()
        // plot(temps)
      });
    }, 5000);
  }
}





  // $("#graphBtn").click(function() {

  //   $('#graphdiv').show();
    
  //   $("#graphBtn" ).hide();
  //   $("#graphBtn").off('click')
  // });
// $("#graphBtn" ).hide();
// $('#graphdiv').hide();





// var svg = d3.select('#graph')
//   .append('div')
//   .attr('class', 'svg-container')
//   .append('svg')
//   .attr("preserveAspectRatio", "xMinYMin meet")   
//   .attr("viewBox", "0 0 400 400")
//    //class to make it responsive
//   .attr('class', "svg-content-responsive", true);

// var temps = [];

// svg.append('line')
//   .attr('class', 'axis')
//   .attr('x1', 30)
//   .attr('y1', 20)
//   .attr('x2', 30)
//   .attr('y2', 271);

// svg.append('line')
//   .attr('class', 'axis')
//   .attr('x1', 29)
//   .attr('y1', 270)
//   .attr('x2', 390)
//   .attr('y2', 270)

// svg.append('text')
//   .attr('class', 'legend')
//   .attr('x', 10)
//   .attr('y', 25)
//   .attr('font-size', 14)
//   .text('25')

// svg.append('text')
//   .attr('class', 'legend')
//   .attr('x', 10)
//   .attr('y', 275)
//   .attr('font-size', 14)
//   .text('15')




// var ymin = 60;
// var w = (390 - 50) / 10 - 2 ;

// function plot(data) {
//   var bar = svg.selectAll('.bar')
//                 .data(data)
//   bar
//     .enter()
//     .append('rect')
//     .attr('class', 'bar')
//     .attr('x', function(d,i){ return (w + 2)*i + 40 })
//     .attr('width', w )
//     .attr('y', 0)

//   bar
//     .attr('y', function(d,i){
//       var y = 269 - 10 * d.value;
//       console.log(y)
//       return y;
//      })
//     .attr('height', function(d,i){
//       var y = 10 * d.value;
//       console.log(y)
//       return y;
//      })


// }


$(document).ready(main);


