'use strict';


var button = document.getElementById('submit')
button.addEventListener("click", addDataToPage)


function doRequest(callback) {
  var x = new XMLHttpRequest();
  x.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts');
  x.onload = function() {
      callback(x.responseText)
  };
  x.send();
}

function handleData(data){
  console.log(data);
}

doRequest(handleData)

 
function addDataToPage() {
    console.log("click event");
    var location = document.getElementById('location').value;
    if (location !== "") {
        getData(location, handleData);
    }
}