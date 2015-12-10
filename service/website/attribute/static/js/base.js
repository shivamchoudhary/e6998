$( document ).ready(function() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
        var data = JSON.parse(xhttp.responseText);
        updateChartMenu(data);
    }
  };
  xhttp.open("GET", "/index/prob/", true);
  xhttp.send();
});

function updateChartMenu(data) {
    var number_data = data.probability;
    for (index = 0; index < number_data.length; ++index) {
        console.log(number_data[index]);
        var current_string = '<li id="';
        current_string = current_string.concat(number_data[index]);
        current_string = current_string.concat('"><a href="#">');
        current_string = current_string.concat(number_data[index]);
        current_string = current_string.concat('</a></li>');
        console.log(current_string);
        $("#prob_menu ul").append(current_string);
        $('#prob_menu li').click(function(e) 
        { 
            loadDoc(this.id);
        });
    }
}

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

function loadDoc(data) {
    var configuration = {};
    configuration["request_prob"] = data;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var data = JSON.parse(xhttp.responseText);
            updateChart(data);
        }
    };
    xhttp.open("POST", "/index/chart/", true);
    console.log(JSON.stringify(configuration));
    xhttp.send(JSON.stringify(configuration));
}

function updateConfiguration() {
    var configuration = {}; 
    configuration["config"] = document.getElementById("config_json").value;
    configuration["sites"] = document.getElementById("config_sites").value;
    configuration["openwpm_dir"] = document.getElementById("openwpm_dir").value;
    configuration["iterations"] = document.getElementById("iter").value;
    configuration["num_browers"] = document.getElementById("num_browser").value;
    configuration["dataObservatory_dir"] = document.getElementById("db_dir").value;
    configuration["fname"] = document.getElementById("file_name").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            window.alert("success!");
        }
    };
    xhttp.open("POST", "/index/configure/", true);
    var json_configuration = JSON.stringify(configuration);
    xhttp.send(json_configuration);
    console.log(json_configuration);
}

var morrisChart = null;

function updateChart(chart_data) {
    var number_data = chart_data.chartInfo;
    var prob_data = chart_data.currentProb;
    console.log(number_data);
    console.log(prob_data);
    config = {
      data: number_data,
      xkey: 'y',
      ykeys: ['s'],
      labels: ['Detected Success Rate'],
      fillOpacity: 0.6,
      hideHover: 'auto',
      behaveLikeLine: true,
      parseTime: false,
      redraw: true,
      resize: true,
      pointFillColors:['#ffffff'],
      pointStrokeColors: ['black'],
      lineColors:['gray','red'],
      goals:[prob_data]
     };
    config.element = 'line-chart';
    if (morrisChart == null) {
        morrisChart = Morris.Line(config);   
    } else {
        morrisChart.setData(config.data);   
    }
}
