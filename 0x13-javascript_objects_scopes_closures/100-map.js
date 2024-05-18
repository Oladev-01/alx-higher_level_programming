#!/usr/bin/node
/* this script maps an array of numbers to a new array
which is the result of the product of each
 elements in the array with its index */

const list = require('./100-data.js').list;

const newList = list.map((num, idx) => num * idx);

console.log(list);
console.log(newList);
