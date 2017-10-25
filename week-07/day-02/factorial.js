'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial


function factorio(factorial) {
  if (factorial === 0) {
    return 1
  } else {
      return factorial * factorio(factorial-1);
  }
}
console.log(factorio(5))

