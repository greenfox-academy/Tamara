'use strict';

var numbers = [2, 3];

var sumNumbers = function (numArray) {
  let sumNums = 0;
  if (numArray !== null) {
    for (let i=0; i<numArray.length;i++) {
      sumNums += numArray[i];
    } return sumNums;
  } else {
     throw new Error('Null object not found');
    };
};

module.exports = sumNumbers;
