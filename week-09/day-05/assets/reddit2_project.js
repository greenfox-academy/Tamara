'use strict';


// var button = document.getElementById('submit')
// button.addEventListener("click", addDataToPage)
var container = document.querySelector('section');

function doRequest(callback) {
  var x = new XMLHttpRequest();
  x.open('GET', 'http://localhost:8080/');
  x.onload = function() {
     var data = JSON.parse(x.responseText).posts;
    callback(data);
  };
  x.send();
}

function handleData(data){
  console.log(data);
  data.forEach(function(element) {
    let blah = document.createElement('div');
    blah.innerHTML = element.title;
    container.appendChild(blah);
    
    let url = document.createElement('a');
    url.setAttribute('href', element.url);
    url.innerHTML = element.url;
    container.appendChild(url);
    console.log(element.url);
  
  });
};

doRequest(handleData)

 
// function addDataToPage() {
//     console.log("click event");
//     var submit = document.getElementById('submit').value;
//     if (location !== "") {
//         getData(location, handleData);
//     }
// }