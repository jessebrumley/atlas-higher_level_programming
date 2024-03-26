#!/usr/bin/node
/*
An instance method that prints the Rectangle defined in task 2
*/
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let output = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        output += 'X';
      }
      if (i < (this.height - 1)) {
        output += '\n';
      }
    }
    console.log(output);
  }
}

module.exports = Rectangle;
