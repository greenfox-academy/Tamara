'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.


var someFruits = fruits.map (function (e, newList) {
  var containEs = [];
  if(e.indexOf('e') !== -1) {
      containEs.push(e);
      newList(containEs);
  };
});

function newList (containEs) {
  console.log(containEs);
};

console.log(someFruits(containEs))