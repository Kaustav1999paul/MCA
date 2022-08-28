
const data = [
    { name: 'A', score: 80 },
    { name: 'B', score: 76 },
    { name: 'C', score: 20 },
    { name: 'D', score: 82 },
    { name: 'E', score: 90 },
    { name: 'F', score: 75 },
    { name: 'G', score: 18 },
    { name: 'H', score: 71 },
    { name: 'I', score: 29 },
    { name: 'J', score: 68 },
    { name: 'K', score: 96 },
    { name: 'L', score: 23 },

  ];

  const svg = d3.select('#d3-container')
    .append('svg')
    .attr('width', 1000)
    .attr('height', 500);
    
  const x = d3.scaleBand()
    .domain(d3.range(data.length))
    .range([50,1000])
    .padding(0.3)

  const y = d3.scaleLinear()
    .domain([0, 120])
    .range([450, 50])

  svg.append("g")
    .selectAll("rect")
    .data(data)
    .join("rect")
    .attr("x", (d, i) => x(i))
    .attr("y", (d) => y(d.score))
    .attr("height", d => y(0) - y(d.score))
    .attr("width", x.bandwidth())
    .attr("fill", 'orange');

  function yAxis(g) {
    g.attr("transform", `translate(50, 0)`)
    .call(d3.axisLeft(y))
    .attr("font-size", '20px')
  }

  function xAxis(g) {
    g.attr("transform", `translate(0,450)`)
      .call(d3.axisBottom(x))
      .attr("font-size", '20px')
  }

  svg.append("g").call(xAxis);
  svg.append("g").call(yAxis);
  svg.node();







//.sort((a, b) => d3.ascending(a.score, b.score))
