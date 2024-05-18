#!/usr/bin/node
/* this script defines a class Square that inherits from Square
and defines a funtion charPrint(c) which prints the square rep
with 'C' or 'X' if c is undefined */

const SquareParent = require('./5-square.js');

class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === 'C') {
      for (let height = 0; height < this.height; height++) {
        for (let width = 0; width < this.width; width++) {
          process.stdout.write('C');
        }
        console.log();
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
