#!/usr/bin/node
/* this script defines a function that reverses a list */

exports.esrever = function (list) {
  const myList = [];
  for (const searched of list) {
    myList.unshift(searched);
  }
  return myList;
};
