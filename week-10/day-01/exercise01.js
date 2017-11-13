'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

// '. solution: with this solution you can't use the says function in our program for other variables.
function says () {
  console.log(this.sound);
};

let Animals = {
  says
};

let cat = {
  sound: 'meaow'
};

Object.setPrototypeOf(cat, Animals);
cat.says();


// 2. solution: with this solution we use huge memory.
const Animals = {
  init: function(says) {
    this.says = says;
  },
  sound: function () {
    console.log('The sound of this animal is  ' + this.says);
  },
};

const dog = Object.create(Animals);
dog.init('wwoooofff');
dog.sound();


//3. solution: this is the best solution. it can use smaller memory and we can create with it smaller objects.
function Animals (says) {
  this.says = says;
};
Animals.prototype.speak = function () {
  console.log(this.says);
};
let bear = new Animals('brrr');
bear.speak();

