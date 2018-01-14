'use strict';

var counter = function (text) {
  let word = text.split('');
  let countedLetters = {};
  word.forEach(element => {
    if (countedLetters[element]) {
      countedLetters[element] += 1;
    } else {
      countedLetters[element] = 1;
    } 
  });
  return countedLetters;
}

module.exports = counter;
