#!/usr/bin/node
/*
A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
*/
const number = process.argv[2];

const parsedNumber = parseInt(number, 10);

if (isNaN(parsedNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsedNumber);
}
