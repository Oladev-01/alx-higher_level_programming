#!/usr/bin/node
/*
this package checks the number of arguments parsed to
the file and run statement based on them
*/
const argCount = process.argv.length;

if (argCount === 2) {
  console.log('No argument');
} else if (argCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
