#!/usr/bin/node
/*
this package return the addition of two number X and Y
where X is he first argument and  Y is the second argument */

function add (a, b) {
  console.log(a + b);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
