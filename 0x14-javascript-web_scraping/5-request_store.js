#!/usr/bin/node
/**
 * this package gets the content of a webpage and
 * write to a file
 */

const request = require('request');
const fs = require('fs');
if (process.argv.length != 4) {
    console.error('Usage: 5-request_store.js <url> <filename>');
    process.exit(1);
}
url = process.argv[2];
fileToWrite = process.argv[3];

request(url, (err, response, body) => {
    if (err) {
        console.error(err);
    }
    if (response.statusCode === 200) {
        const data = JSON.parse(body);
        fs.writeFile(fileToWrite, data, (err) => {
            if (err) {
                console.error('Error:', err);
            }
        });
    }
});
