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

