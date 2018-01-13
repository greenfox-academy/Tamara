'use strict';

const url = 'http://localhost:8080/';
var tableElement = document.querySelector('tbody');
const searchButton = document.querySelector('#submit');
const nameInput = document.querySelector('#category');

function ajax (command, url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(command, url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status === 200) {
        console.log(xhr.responseText);
          callback(JSON.parse(xhr.responseText));
      };
  };
  xhr.send();
};

let renderBook = function(item) {
  item.forEach(function(item) {
      let tempBook = document.createElement('li');
      tempBook.innerText = item.book_name;
      document.body.appendChild(tempBook);
  });
};


let listDetails = function (response) {
  response.forEach(function(element) {
    const listData = '<tr><td>' + element.book_name +
        '</td><td>' + element.aut_name +
        '</td><td>' + element.cate_descrip +
        '</td><td>' + element.pub_name +
        '</td><td>' + element.book_price +
        '</td></tr>';
    tableElement.innerHTML += listData;
  });
};

// let searchedBooks = function (results, callback) {
//   ajax('GET', results, callback)
// }
searchButton.addEventListener('click', click)

function click() {
  console.log("click event")
  var searchedElement = nameInput.value;
  if (searchedElement !== "") {
      ajax('GET', url + `books/?category=${searchedElement}`, listDetails);
  }
}
ajax('GET', url + 'books/', renderBook);
