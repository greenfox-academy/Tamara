'use strict';

const ajax = function(method, endpoint, data, callback) {
  var x = new XMLHttpRequest();
  x.open(method, 'http://localhost:8080'+ endpoint);
  x.setRequestHeader('Content-Type', 'application/json');
  x.onload = function() {
     var data = JSON.parse(x.responseText);
     console.log(data)
    callback(data);
  };
  x.send(JSON.stringify(data));
};


