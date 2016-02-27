var main = function() {
// insert code here
$(".TemperatureButton").click(function() {

    $.ajax({
            url: "/temperature",
            type: "get",
        }).done(function (data) {

        $( ".TemperatureButton" ).text( data.value );

    });
});
};

$(document).ready(main);


