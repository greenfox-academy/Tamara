'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says


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
// Animals.prototype.laud = function(say) {
//   console.log('brrrrr');
// }

// var dog = new Animals('wooof');
// console.log(dog.laud());

