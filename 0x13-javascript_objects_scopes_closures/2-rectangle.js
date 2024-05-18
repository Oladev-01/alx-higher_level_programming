#!/usr/bin/node
/*
this script defines a script that instantiates intsance
of the class with two args w and h, if either of the class
 is <= 0, it returns an empty object */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
