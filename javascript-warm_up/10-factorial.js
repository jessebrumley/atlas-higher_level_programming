#!/usr/bin/node
/*
A script that computes and prints a factorial
*/
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(Number(process.argv[2])));
