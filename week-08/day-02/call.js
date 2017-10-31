'use strict';

function factorialTillLimitWithCallback(limit, stopPrinting) {
  var factorial = 1;
  for (var i = 1; i <= limit; ++i) {
    callback(factorial);
    factorial *= i;
  }
}

function stopPrinting(limit) {
  limit = 20;
  console.log(factorial);
}
factorialTillLimitWithCallback(stopPrinting);

// Create a function and pass it as a parameter to the factorialTillLimitWithCallback
// function, and print all the factorial numbers till 20