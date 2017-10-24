'use strict';

let currentHours = 14;
let currentMinutes = 34;
let currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

let day_hours = 24;
let day_minutes = 0;
let day_seconds = 0;

let remaining_hours = day_hours - currentHours;
let remaining_minutes = day_minutes - currentMinutes;
let remaining_seconds = day_seconds - currentSeconds;

let remaining = remaining_hours * 60 * 60 + remaining_minutes * 60
let remaining_total = remaining + remaining_seconds

console.log(remaining_total);