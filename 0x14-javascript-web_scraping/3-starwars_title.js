#!/usr/bin/node
/**
 * getting the title with eacho star wars episodes
 * this is possible by requesting from the star wars API
 */

const request = require('request');
const epId = process.argv[2];

if (!epId) {
  console.error('Usage: ./3-starwars_title.js <id>');
  process.exit();
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${epId}`;

request(apiUrl, (err, response, body) => {
  const data = JSON.parse(body);
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (response.statusCode === 200) {
    console.log(data.title);
  } else {
    console.error('Error:', data.detail || 'there was an error in getting resource');
  }
});
