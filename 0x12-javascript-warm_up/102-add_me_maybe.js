#!/usr/bin/node
/*
this package increments and call a function */

function addMeMaybe (number, theFuntion) {
  number++;
  theFuntion(number);
}
module.exports.addMeMaybe = addMeMaybe;
