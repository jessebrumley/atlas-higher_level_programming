#!/usr/bin/node
/*
A script that prints a square
*/
const input = process.argv[2];
const squareSize = parseInt(input, 10);
let output = '';

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < squareSize; row++) {
    for (let col = 0; col < squareSize; col++) {
      output += 'X';
    }
    if (row < squareSize - 1) {
      output += '\n';
    }
  }
  console.log(output);
}
