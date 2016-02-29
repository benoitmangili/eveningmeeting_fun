

var margin = {top: 20, right: 20, bottom: 20, left: 40},
    width = 800 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

var d3_data = d3.range(10).map( function(){ return {value: 20, time: 0 } } );


var svg = d3.select('#graph')
  .append('div')
  .attr('class', 'svg-container')
  .append('svg:svg')
  .attr("preserveAspectRatio", "xMinYMin meet")   
  .attr("viewBox", "0 0 800 800")
   //class to make it responsive
  .attr('class', "svg-content-responsive", true)
  // .attr("width", width + margin.left + margin.right)
  // .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var minTemp = 15;
// var minDate = new Date( 1000 * d3.min(data, function(el){return el.date}) );
// var maxDate = new Date( 1000 * d3.max(data, function(el){return el.date}) );
var xScale = d3.scale.linear()
          .domain([0, 9])
          .range([0, width]);

var yScale = d3.scale.linear()
          .domain([minTemp, 25])
          .range([height, 0]);

svg.append("defs").append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", width)
    .attr("height", height);

var xAxis = d3.svg.axis().orient('bottom').scale(xScale);
var yAxis = d3.svg.axis().orient('left').scale(yScale);

var line = d3.svg.line()
  .x(function(d,i){ 
    // console.log(xScale(i))
    return xScale(i);
  })
  .y(function(d,i){
    // console.log(" ? ",d)
    return yScale(18 + d.value + Math.random());
  })

var min_line = svg.append('path')
                  .attr('d', "M "+xScale(0)+" " + yScale(17) + " L"+xScale(10)+" " +yScale(17)+ " Z")
                  .attr('class', 'min_line hidden');

var max_line = svg.append('path')
                  .attr('d', "M "+xScale(0)+" " + yScale(23) + " L"+xScale(10)+" " +yScale(23)+ " Z")
                  .attr('class', 'max_line hidden');



svg.append('g')
  .attr('class', 'x axis')
  .attr('transform', 'translate(0,'+yScale(minTemp)+')')
  .call(xAxis)

svg.append('g')
  .attr('class', 'y axis')
  // .attr('transform', 'translate(0,'+yScale(0)+')')
  .call(yAxis)

var path = svg.append('g')
  .attr('clip-path', 'url(#clip)')
  .append('path')
  .datum(d3_data)
  .attr('class', 'line')
  .attr('d', line);

var update_limits = function(data){
  min_line.attr('d', "M "+xScale(0)+" " + yScale(data.min_temp) + " L"+xScale(10)+" " +yScale(data.min_temp)+ " Z");
  max_line.attr('d', "M "+xScale(0)+" " + yScale(data.max_temp) + " L"+xScale(10)+" " +yScale(data.max_temp)+ " Z");
  min_line.classed('hidden', false);
  max_line.classed('hidden', false);
}

var plot = function( data, tempo ){
  // console.log('tick', data)
  if (data.with_limits){
    min_line.classed('hidden', false);
    max_line.classed('hidden', false);
  }
  d3_data.push(data.datum);

  path
      .attr('d', line)
      .attr("transform", null)
      .transition()
      .duration(tempo/2)
      .ease("linear")
      .attr("transform", "translate(" + xScale(-1) + ",0)")

  d3_data.shift();  
}