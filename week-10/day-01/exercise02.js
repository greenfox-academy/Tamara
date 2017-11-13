'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference


function Rectangles(oneSide, twoSide) {
  this.oneSide = oneSide;
  this.twoSide = twoSide;
};

Rectangles.prototype.getArea = function() {
  console.log(this.oneSide * this.twoSide);
};

Rectangles.prototype.getCircumference = function() {
  console.log(this.oneSide*2 + this.twoSide*2);
};


let square = new Rectangles(2, 2);
square.getArea();
square.getCircumference();
