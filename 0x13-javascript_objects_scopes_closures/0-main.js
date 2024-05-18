#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log("Normal")
r1.print()

r1.double()
console.log("Doubled")
r1.print()

r1.rotate()
console.log("Rotated")
r1.print()