#!/usr/bin/node
/*
this package computes the factorial of a number parsed as
argument to the package */

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0 || n === 1) { return 1; }
  return n * factorial(n - 1);
}
const arg = process.argv[2];
console.log(factorial(arg));
