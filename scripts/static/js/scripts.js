var main = function() {
// insert code here
$(".OnButton").click(function() {

    // Create Json object
    var json_on  = {"state":"High"};

    $.ajax({
            url: "/lamp",
            type: "put",
            data: json_on
        }).done(function (data) {

        // Only turn on the LED image on the website if the server turned on the real one
        if (data.state === 'High'){
        $(".circle").removeClass("off").addClass("on");

        }
    });
});

$(".OffButton").click(function() {
    // Create Json object

    var json_off = {"state":"Low"};

    $.ajax({
            url: "/lamp",
            type: "put",
            data: json_off
        }).done(function (data) {

        // Only turn on the LED image on the website if the server turned on the real one
        if (data.state === 'Low'){
        $(".circle").removeClass("on").addClass("off");
        }
    });
});
};

$(document).ready(main);


