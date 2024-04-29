#!/usr/bin/node
/*
this package checks for the largest integer among list
of integers parsed as arguments to the file */
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
}

let secLargest = parseInt(args[3]);
let larGest = parseInt(args[2]);

if (secLargest > larGest) {
  const tmp = larGest;
  larGest = secLargest;
  secLargest = tmp;
}
for (let i = 4; i < args.length; i++) {
  const num = parseInt(args[i]);
  if (num > larGest) {
    secLargest = larGest;
    larGest = num;
  } else if (num > secLargest) {
    secLargest = num;
  }
}
console.log(secLargest);
