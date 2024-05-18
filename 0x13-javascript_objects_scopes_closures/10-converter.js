#!/usr/bin/node

/* this script converts a number to a given base */

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
