#!/usr/bin/node
/**
 * this package displays the status code of a GET request
 */

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
    if (err) {
        console.error(err);
    }
});
