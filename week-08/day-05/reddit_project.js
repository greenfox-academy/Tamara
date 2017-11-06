'use strict';


// var button = document.getElementById('submit')
// button.addEventListener("click", addDataToPage)


function doRequest(callback) {
  var x = new XMLHttpRequest();
  x.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts');
  x.onload = function() {
     var data = JSON.parse(x.responseText).posts;
    callback(data);
  };
  x.send();
}

function handleData(data){
  console.log(data);
  let blah = document.createElement('a');
  blah.href = data.title;
  document.body.appendChild(blah);

  let blah2 = document.createElement('a');
  blah2.href = data.title;
  document.body.appendChild(blah2);

}

doRequest(handleData)

 
// function addDataToPage() {
//     console.log("click event");
//     var submit = document.getElementById('submit').value;
//     if (location !== "") {
//         getData(location, handleData);
//     }
// }