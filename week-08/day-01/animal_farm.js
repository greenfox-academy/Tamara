class Animal {
  constructor (hunger, thirst) {
    this.hunger = hungry;
    this.thirst = thirsty;
  }
  eat () {
    this.hunger -= 1;
  }
  drink () {
    this.thirst -= 1;
  }

  play () {
    this.hunger += 1;
    this.thirst += 1;
  }
}


class Farm {
  constructor () {
    this.animals = [];
  }

  breed () {
    for (let i = 1; i <= this.animals.length; i++) {
      if (this.animals.length < 20) {
      this.animals.push(new Animal(5, 5));
      }
    }
  }
  
  slaughter () {
    this.animals.forEach (function(element) {
      // if 
    })

    }
  }


const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 20 Animal objects

const button = document.querySelector('button');

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full