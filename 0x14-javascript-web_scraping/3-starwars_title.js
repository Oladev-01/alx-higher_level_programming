#!/usr/bin/node
/**
 * getting the title with eacho star wars episodes
 * this is possible by requesting from the star wars API
 */

const request = require('request');
ep_id = process.argv[2];

if (!ep_id) {
  console.error('Usage: ./3-starwars_title.js <id>');
  process.exit;
}

apiUrl = `https://swapi-api.alx-tools.com/api/films/${ep_id}`;

request(apiUrl, (err, response, body) => {
  const data = JSON.parse(body);
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (response.statusCode == 200) {
    console.log(data.title);
  } else {
    console.error('Error:', data.detail || 'there was an error in getting resource');
  }
});
