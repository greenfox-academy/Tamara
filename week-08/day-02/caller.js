'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array

function selectLastEvenNumber (nums, printNumber) {
  var num = 0;
  nums.forEach(function (element) {
    if (element % 2 === 0) {
      num = element;
    };
  });
  printNumber(num);
};


function printNumber(num) {
  console.log(num);
};


selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8