'use strict';

const ajax = function(endpoint, callback) {
  var x = new XMLHttpRequest();
  x.open('GET', 'http://localhost:8080'+ endpoint);
  x.setRequestHeader('Content-Type', 'application/json');
  x.onload = function() {
     var data = JSON.parse(x.responseText);
    callback(data);
  };
  x.send();
};


