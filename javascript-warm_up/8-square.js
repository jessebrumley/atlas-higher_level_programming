#!/usr/bin/node
/*
A script that prints a square
*/
const input = process.argv[2];
const squareSize = parseInt(input, 10);
let row = 1;
let col = 1;
let output = '';
if (isNaN(squareSize)) {
  console.log('Missing size');
} else if (row != squareSize) {
  for (row = 1; row < squareSize; row++) {
    for (col = 1; col <= squareSize; col++) {
      output += 'X';
    }
    output += '\n';
  }
} else {
  for (let colFinal = 1; colFinal <= squareSize; colFinal++) {
    output += 'X';
  }
}
console.log(output);
