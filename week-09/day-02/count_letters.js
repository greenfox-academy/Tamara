'use strict';

var counter = function (text) {
  let counted_letters = [];
  for (let i = 0; i <= text.length; i++) {
    if (text !== -1) {
      counted_letters[i] += 1;
  } else {
      counted_letters[i] = 1;
    } return counted_letters;
  };
};


module.exports = counter;