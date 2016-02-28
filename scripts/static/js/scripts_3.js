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
    $("#graphBtn" ).hide();
    $("#graphBtn").off('click')
    start_plot_loop();
  });
};
var tempo = 1000;
var start_plot_loop = function() {
    graphInterval = setInterval(function() {
      $.ajax({
              url: "/temperature",
              type: "get",
      }).done(function (data) {
        plot({datum: data}, tempo)
      });
    }, tempo);
}



$("#graphBtn" ).hide();
$('#graphdiv').hide();

$(document).ready(main);


