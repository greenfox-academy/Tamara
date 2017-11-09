'use strict';
const url = 'http://localhost:3000/';

const ajax = ( method, data, resource, callback ) => {
  const xhr = new XMLHttpRequest();
  data = data ? data : null;
  xhr.open( method, url + resource );
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send( JSON.stringify(data) );
  xhr.onreadystatechange = () => {
    if ( xhr.readyState === 4 ) {
      console.log(JSON.parse(xhr.response));
      callback( JSON.parse(xhr.response) );
    }
  };
};

const renderBooks = function books () {
  books.forEach( function (book) {
    const tempBooks = document.createElement('div');
    tempBooks.innerText = books.book_name;
    document.body.appendChild(tempBooks);
  });
}

ajax('GET', renderBooks);