#!/usr/bin/node
/*
this script defines a function that returns the number of
occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const searched of list) {
    if (searched === searchElement) {
      count++;
    }
  }
  return count;
};
