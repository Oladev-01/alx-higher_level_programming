#!/usr/bin/node
/*
this script define a class Square which inherits from class Rectangle */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
