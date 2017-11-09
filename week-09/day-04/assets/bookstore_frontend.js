'use strict';

const url = 'http://localhost:8080/';

function ajax (command, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(command, url + 'books', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
      if(xhr.readyState == 4 && xhr.status === 200) {
        console.log(xhr.responseText);
          callback(JSON.parse(xhr.responseText));
      };
  };
  xhr.send();
};

let renderBook = function(item) {
  item.forEach(function(item) {
      let tempBook = document.createElement('p');
      tempBook.innerText = item.book_name;
      document.body.appendChild(tempBook);
  });
};


ajax('GET', renderBook);