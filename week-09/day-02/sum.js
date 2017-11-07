var numbers = [2, 3];

var sum = function (numbers) {
  let sumNums = 0;
  for (let i=0; i<numbers.length;i++) {
    sumNums += numbers[i];
  }
  return sumNums;
};

module.exports = sum;