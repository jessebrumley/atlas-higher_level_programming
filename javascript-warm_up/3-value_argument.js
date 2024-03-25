#!/usr/bin/node
/*
A script that prints the first argument passed to it
*/
const args = process.argv.slice(2);

try {
  for (const arg of args) {
    console.log(arg);
  }
} catch (error) {
  console.log('No arguement');
}
