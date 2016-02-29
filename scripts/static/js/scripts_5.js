
var display_twitts = function( data, tempo ){
  console.log(data)
  // console.log('tick', data)
  // if (data.with_limits){
  //   min_line.classed('hidden', false);
  //   max_line.classed('hidden', false);
  // }
  d3_data.push(data);

  selection
    .text(function(d){
      return '' + d.vote + ' ' + d.author;
    })
  // path
  //     .attr('d', line)
  //     .attr("transform", null)
  //     .transition()
  //     .duration(400)
  //     .ease("linear")
  //     .attr("transform", "translate(" + xScale(-1) + ",0)")

  d3_data.shift();  
}

var d3_data = d3.range(10).map( function(){
  return {
            "author":    'benoit',
            "tweet":     'grrrr',
            "timeStamp": '?',
            "vote":      'Hot',
          };
} );


var selection = d3
          .select('#messages ul')
          .selectAll('.twitts')
          .data(d3_data);

selection//.enter()
  .append('li')
  .attr('class', '.twitts')
  .text(function(d){ 
    return ":" + d; 
  })

  // selection.exit()
  //   .text(function(d, i){
  //     console.log("removing ", i, " -> ",d)
  //   })
  //   .remove()

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('new_tweet', function(data) {
  display_twitts(data)
});





$('#btn').click(function(){
  console.log('click')
  // setInterval(function(){
    $.ajax({url:'http://' + document.domain + ':' + location.port + '/newtweet'});
  // }, 1000)
})




// $(document).ready();


