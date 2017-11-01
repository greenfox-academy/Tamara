'use strict'

let button = document.getElementById('delayed');
let answer = document.getElementById('answer');

function writeASentence () {
  setTimeout(function() {
    answer.innerHTML = `2 seconds ellapsed`;
  }, 2000); 

};
button.addEventListener('click', writeASentence);





