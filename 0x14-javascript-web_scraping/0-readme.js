#!/usr/bin/node
/**
 * this package reads and displays the content of a
 * file to stdout
 */

const { error } = require('console');
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  // reading from the file, the (err, data) serves as a error call back function
  if (err) {
    error(err);
    return;
  }
  console.log(data);
});
