#!/usr/bin/node
/*
this package prints a square X times where X
 is the number parsed as arg to the file */

let numTimes = process.argv[2];

if (!isNaN(numTimes) && Number.isInteger(Number(numTimes))) {
  numTimes = parseInt(numTimes, 10);
} else {
  console.log('Missing size');
}

for (let i = 1; i <= numTimes; i++) {
  for (let j = 1; j <= numTimes; j++) {
    process.stdout.write('X');
  }
  console.log('');
}
