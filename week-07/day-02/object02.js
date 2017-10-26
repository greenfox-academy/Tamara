'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average


function moreCandies(student) {
  let sum = [];
  student.forEach(function(e) {
    if (e.candies > 4) {
      sum.push(e.name);
    }
});
  return sum
}

console.log(moreCandies(students))
      
function avgCandies(student) {
  let sum = 0;
  var avgSum = 0;
  student.forEach(function(e) {
    sum += e.candies;
});
  return avgSum = sum / 2;
}

console.log(avgCandies(students))