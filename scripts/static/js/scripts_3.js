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
    $("#graphBtn" ).hide().off('click')
    $("#temperatureBtn").off('click')
    start_plot_loop();
  });
};
var tempo = 2000;
var start_plot_loop = function() {
    graphInterval = setInterval(function() {
      $.ajax({
              url: "/temperature",
              type: "get",
      }).done(function (data) {
        plot({datum: data}, tempo);
        $( "#current_temperature" ).text( data.value.toFixed(2) + "°C" );

      });
    }, tempo);
}



$("#graphBtn" ).hide();
$('#graphdiv').hide();

$(document).ready(main);


