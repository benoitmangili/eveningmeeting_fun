var main = function() {
// insert code here
$(".TemperatureButton").click(function() {

    $.ajax({
            url: "/temperature",
            type: "get",
        }).done(function (data) {

        $( ".current_temperature" ).text( data.value + "degC" );

    });
});
};

$(document).ready(main);


