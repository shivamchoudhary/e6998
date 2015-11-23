function QueryData(data)
{
   var ret = [];
   for (var d in data)
      ret.push(d + "=" + data[d]);
   return '?' + ret.join("&");
}

function updateUrl() {
    var data = readInput();
    var baseUrl = document.getElementById("testUrl");
    baseUrl += QueryData(data);
    document.getElementById("testUrl").href = baseUrl;
}

function readInput() {
    var country = document.getElementById("inputForms");
    var inputs = country.getElementsByTagName('input');
    var dict = {};
    for (index = 0; index < inputs.length; ++index) {
        dict[inputs[index].id] = inputs[index].value;
    }
    return dict;
}

function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
        var data = JSON.parse(xhttp.responseText);
        updateChart(data);
    }
  };
  xhttp.open("GET", "/index/chart/", true);
  xhttp.send();
}

var morrisChart = null;

function updateChart(chart_data) {
    var number_data = chart_data.chartInfo;
    console.log(number_data);
    config = {
      data: number_data,
      xkey: 'probability',
      ykeys: ['numberOfSuccess'],
      labels: ['Detected P'],
      fillOpacity: 0.6,
      hideHover: 'auto',
      behaveLikeLine: true,
      resize: true,
      parseTime: false,
      pointFillColors:['#ffffff'],
      pointStrokeColors: ['black'],
      lineColors:['gray','red']
     };
    config.element = 'line-chart';
    if (morrisChart == null) {
        morrisChart = Morris.Line(config);   
    } else {
        morrisChat.setData(config);
    }
}
