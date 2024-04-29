#!/usr/bin/node
/*
this package prints "C is fun" X times where x
is the argument parsed to the file
*/

const string = 'C is fun';
let numTimes = process.argv[2];

if (!isNaN(numTimes) && Number.isInteger(Number(numTimes))) {
  numTimes = parseInt(numTimes, 10);
} else {
  console.log('Missing number of occurrences');
}
for (let i = 1; i <= numTimes; i++) {
  console.log(string);
}
