#!/usr/bin/node
/*
A script that searches the second biggest integer in the list of arguments
*/
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numberArray = process.argv.slice(2).map(Number);
  const secondBiggest = numberArray.sort(function (a, b) { return b - a; })[1];
  console.log(secondBiggest);
}
