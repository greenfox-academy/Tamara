'use strict';

var lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

for (let i = 0; i <= lineCount-1; i++) {
  if (i === 0 || i === lineCount-1) {
    console.log(Array(lineCount+1).join("%"))
  } else {
    console.log("%" + Array(i).join(" ") + "%" + Array(lineCount-1-i).join(" ") + "%");
  }
}'use strict';

var lineCount = 4;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

for (let i = 0; i <= lineCount+1; i++) {
  if (i === 0 || i === lineCount+1) {
    console.log(Array(lineCount+2).join("%"))
  } else {
    console.log("%" + Array(i).join(" ") + "%" + Array(lineCount-i).join(" ") + "%");
  }
}