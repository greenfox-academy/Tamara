'use strict';

let currentHours = 14;
let currentMinutes = 34;
let currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

let dayHours = 24;
let dayMinutes = 0;
let daySeconds = 0;
let remainingHours = dayHours - currentHours;
let remainingMinutes = dayMinutes - currentMinutes;
let remainingSeconds = daySeconds - currentSeconds;
let remaining = remainingHours * 60 * 60 + remainingMinutes * 60
let remainingTotal = remaining + remainingSeconds

console.log(remainingTotal);