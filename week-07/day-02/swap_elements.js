'use strict';
// - Create a variable named `abc` with the following content: `["Arthur", "Boe", "Chloe"]`
// - Swap the first and the third element of `abc`

let abc = ["Arthur", "Boe", "Chloe"]

function change() {
  [abc[0], abc[2]] = [abc[2], abc[0]];
  return abc;
}

console.log(change())
