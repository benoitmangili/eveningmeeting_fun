
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
$('.graphrow').hide();
$('.bulb svg #star').hide();
$('.bulb svg #grad_on').hide();


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
    $('#start_controller').off('click').hide();
    controllerIsRunning = true;
    $('.graphrow').show();
    


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
    $('#min_value div').html(min_temp)
    $('#max_value div').html(max_temp)
    update_limits({min_temp, max_temp});
  }

var update_set_point_min_up   = function(){ update_set_point(min_temp+0.5, max_temp  ); }
var update_set_point_min_down = function(){ update_set_point(min_temp-0.5, max_temp  ); }
var update_set_point_max_up   = function(){ update_set_point(min_temp  , max_temp+0.5); }
var update_set_point_max_down = function(){ update_set_point(min_temp  , max_temp-0.5); }

var tempo = 2000;
var start_plot_loop = function() {
  if (!controllerIsRunning){
    graphInterval = setInterval(function() {
      $.ajax({
              url: "/temperature",
              type: "get",
      }).done(function (data) {
        // data.value += 18 + Math.random();
        plot({datum: data, with_limits:true}, tempo)
      });
    }, tempo);

    graphInterval = setInterval(function() {
      $.ajax({
              url: "/lamp",
              type: "get",
      }).done(function (data) {
        console.log("lamp : ", data);
        if (data.state === 'Low') {
          $('.bulb svg #star').hide();
          $('.bulb svg #grad_on').hide();
        } else {
          $('.bulb svg #star').show();
          $('.bulb svg #grad_on').show();
        }
      });
    }, tempo);


  }
}

$(document).ready(main);


