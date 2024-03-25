#!/usr/bin/node
/*
A script that computes and prints a factorial
*/
function factorial (a) {
  let result = parseInt(0);
  for (let i = 0; i <= a; i++) {
    result += i;
  }
  console.log(result);
}

factorial(Number(process.argv[2]));
