


function display_twitts(data) {

  var selection = d3
            .select('#messages ul')
            .selectAll('.twitts')
            .data(data);
  
  selection.enter()
    .append('li')
    .attr('class', '.twitts')
    .text(function(d){ 
      return ":" + d; 
    })

  selection.exit()
    .text(function(d, i){
      console.log("removing ", i, " -> ",d)
    })
    .remove()

}


var twitts = [];

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('new_tweet', function(data) {
  console.log(' >>> ',data)

  if (twitts.push( {text: data} ) > 10 ) twitts.shift()


  console.log(twitts)
 display_twitts(twitts)
});





$('#btn').click(function(){
  console.log('click')
  // setInterval(function(){
    $.ajax({url:'http://' + document.domain + ':' + location.port + '/newtweet'});
  // }, 1000)
})




// $(document).ready();


