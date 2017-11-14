'use strict';

function ajax(endpoint, callback) {
  var x = new XMLHttpRequest();
  x.open('GET', 'http://localhost:8080/'+ endpoint);
  x.onload = function() {
     var data = JSON.parse(x.responseText);
    callback(data);
  };
  x.send();
};

ajax(endpoint, callback);

