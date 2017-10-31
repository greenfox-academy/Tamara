'use strict';

function factorialTillLimitWithCallback(limit, stopPrinting) {
  var factorial = 1;
  for (var i = 1; i <= limit; ++i) { 
    if (limit <= 20) {
      factorial *= i;
      stopPrinting(factorial);
    }
  }
}

function stopPrinting(factorial) {
    console.log(factorial);
}

factorialTillLimitWithCallback(5, stopPrinting);

// Create a function and pass it as a parameter to the factorialTillLimitWithCallback
// function, and print all the factorial numbers till 20