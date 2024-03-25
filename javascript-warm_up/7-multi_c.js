#!/usr/bin/node
/*
A script that prints x times “C is fun”
*/
const x = process.argv[2];

const parsedX = parseInt(x, 10);

if (isNaN(parsedX)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsedX; i++) {
    console.log('C is fun');
  }
}
