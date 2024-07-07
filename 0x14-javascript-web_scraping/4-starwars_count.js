#!/usr/bin/node
/**
 * getting the number of movies where the character “Wedge Antilles”
 *  is starred. This is possible by requesting from the star wars API
 */

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <api>');
  process.exit();
}
request(apiUrl, (err, response, body) => {
  const data = JSON.parse(body);
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (response.statusCode === 200) {
    const result = data.results;
    let count = 0;
    result.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('/api/people/18/')) {
          count += 1;
        }
      });
    });
    console.log(count);
  } else {
    console.error('Error:', data.detail || 'there was an error in getting resource');
  }
});
