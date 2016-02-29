var update_bulb = function (state) {
    // Only turn on the LED image on the website if the server turned on the real one
    if (state === 'Low'){
        $('.bulb svg #star').hide();
        $('.bulb svg #grad_on').hide();
    } else {
        $('.bulb svg #star').show();
        $('.bulb svg #grad_on').show();
    }
}

var blub_setter = function(state) {
    return function() {
        // Create Json object
        var json_off = {"state":state};

        $.ajax({
                url: "/lamp",
                type: "put",
                data: JSON.stringify(json_off),
                contentType: "application/json; charset=utf-8",
        })
        .then(function (data) {
            update_bulb(data.state);
        });
    }
}

var main = function() {
    $(".OnButton").click(blub_setter('High'));
    $(".OffButton").click(blub_setter('Low'));
};

update_bulb('Low');

$(document).ready(main);


