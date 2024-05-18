#!/usr/bin/node
/*
this script defines a Rectangle class and prints the
Rectangle using x notation based on the width and height
provided */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let height = 0; height < this.height; height++) {
      for (let width = 0; width < this.width; width++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

module.exports = Rectangle;
