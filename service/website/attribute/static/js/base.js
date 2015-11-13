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

$(function() {

var data = [
      { y: '0.6', a: 90,  b: 70},
      { y: '0.7', a: 50, b: 90},
      { y: '0.8', a: 65,  b: 75},
      { y: '0.9', a: 50,  b: 50},
      { y: '1.0', a: 160, b: 95}
    ],
    config = {
      data: data,
      xkey: 'y',
      ykeys: ['a', 'b'],
      labels: ['Detected P', 'Generated P'],
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
Morris.Line(config);
});
