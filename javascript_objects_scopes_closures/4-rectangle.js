#!/usr/bin/node
/*
An instance method that rotates the Rectangle from task 3 and another that doubles it's size
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
  rotate () {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
