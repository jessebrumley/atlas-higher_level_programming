#!/usr/bin/node
/*
A class Square that defines a square and inherits from Square of 5-square.js and an instance method that prints it
*/
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    let output = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        output += c;
      }
      if (i < this.size - 1) {
        output += '\n';
      }
    }
    console.log(output);
  }
}

module.exports = Square;
