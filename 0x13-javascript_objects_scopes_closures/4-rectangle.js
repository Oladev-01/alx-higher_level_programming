#!/usr/bin/node
/*
this script defines a class Rectangle with methods:
```print```: prints the representation of the Rectangle with 'X'
```Double```: this doubles the value of the parameters of the Rectangle
```Rotate```: this exchanges the parameters of the rectangle */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
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
