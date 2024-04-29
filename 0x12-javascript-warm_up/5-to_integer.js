#!/usr/bin/node
/*
this package prints the format My number: <arg> if
arg is a number or a string of number
*/

const arg = process.argv[2];

if (!isNaN(arg) && Number.isInteger(Number(arg))) {
  console.log('My number: ' + parseInt(arg, 10));
} else {
  console.log('Not a number');
}
