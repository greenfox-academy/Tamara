'use strict';

let button = document.querySelector('button');
let result = document.querySelector('p');
let list = document.querySelectorAll('li');

let counter = function() {
  result.textContent = 'Totally: ' + list.length;
};

button.addEventListener('click', counter);
