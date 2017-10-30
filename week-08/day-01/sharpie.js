class Sharpie {
  constructor(color, width) {
    this.color = color;
    this.width = width;
    this.inkAmount = 100;
  }
  use () {
    this.inkAmount -= this.width;
    return this.inkAmount;
  }
}
var Sharpie1 = new Sharpie ("blue", 10);

let counter = function () {
  let timesCounter = 0;
    while (Sharpie1.inkAmount > 0) {
      Sharpie1.use();
      console.log(Sharpie1.inkAmount);
      timesCounter +=1;
    } console.log(timesCounter);
}



counter()

