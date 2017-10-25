'use strict';
// - Create an array named `s` with the following content: `[1, 2, 3, 8, 5, 6]`
// - Change the 8 to 4 with the `.map` method 
// - Print the fourth element as a test

let s = [1, 2, 3, 8, 5, 6]
let newS = s.map(function(num) {
  if (num === 8) {
    num = 4;
  }
  return num;
});

console.log(newS[3])

