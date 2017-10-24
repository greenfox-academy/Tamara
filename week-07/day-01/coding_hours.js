'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

let coding_hours = 17 * 5 * 6; 
console.log(coding_hours);

let weekly_hours = 5 * 6;
let weekly_work_hours = 52;
console.log(weekly_hours / weekly_work_hours * 100 + ' %')