#!/usr/bin/node
/**
 * this package displays the status code of a GET request
 */

const request = require('request');
const urlPath = process.argv[2];

// using the request module to query the url
request(urlPath, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  }
  console.log('code:', response.statusCode);
});
