'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];


for (let i = 0; i <= boys.length; i++) {
  if (i <= girls.length) {
    order.push(girls[i]);
    order.push(boys[i]);
  } else { 
      order.push(boys[i]);
    }
} 

console.log(order);