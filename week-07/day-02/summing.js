'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

let num = 5

function sum (num) {
  let addNum = 0;
  for (let i = 0; i <= num; i++) {  
    addNum += i;
    
  }
  return addNum;
}

console.log(sum(num))