'use strict';
// - Create a variable named `p1`
//   with the following content: `[1, 2, 3]`
// - Create a variable named `p2`
//   with the following content: `[4, 5]`
// - Log to the console if `p2` has more elements than `p1`


let p1 = [1, 2, 3]
let p2 = [4, 5]

function compare () {
  if (p2.length > p1) {
    console.log('more');
  } else {
    console.log('less');
  }
}

compare()