function buildPlot() {

  
const url = "/predict";
d3.json(url).then(function(response) {

  console.log(response);

  const data = response;

  fig = px.line(x=data["ds"], y=data["yhat"], title="sample figure")
      print(fig)
  fig.show("plot")
  
});
}

buildPlot();


  



