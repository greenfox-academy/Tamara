'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies


function studentListing (student) {
  student.forEach(function(e) {
    console.log(e.name, "has", e.candies, "candies")
  });
}

studentListing(students)

function sum_of_candies(student) {
  let sum = 0;
  student.forEach(function(e) {
      if (e.candies < 5) {
          sum += e.age;
      }
  });
  return sum
}

console.log(sum_of_candies(students))

