#!/usr/bin/node
/*
A script that prints a square
*/
const input = process.argv[2];

const squareSize = parseInt(input, 10);

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  let output = '';
  for (let col = 0; col < squareSize; col++) {
    for (let row = 0; row < squareSize; row++) {
      output += 'X';
    }
    output += '\n';
  }
  console.log(output);
}
