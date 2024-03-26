#!/usr/bin/node
/*
A class Rectangle defined in task one except this creates an empty class if either arguement is 0 or lower
*/
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
