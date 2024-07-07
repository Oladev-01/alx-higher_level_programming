#!/usr/bin/node
/**
 * this script prints all the characters in a star war
 * movie. episode is specified by the Id
 */

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      }
      if (response.statusCode === 200) {
        resolve(JSON.parse(body));
      }
    });
  });
}

request(apiUrl, async (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  try {
    const characterNames = await Promise.all(film.characters.map(url => fetchCharacter(url)));
    characterNames.forEach(names => { console.log(names.name); });
  } catch (err) {
    console.error(err);
  }
});
