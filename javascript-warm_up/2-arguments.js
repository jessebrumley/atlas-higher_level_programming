#!/usr/bin/node
/*
A script that prints a message depending of the number of arguments passed
*/
if (process.argv.length <= 2) {
  console.log('No arguement');
} else if (process.argv.length === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
