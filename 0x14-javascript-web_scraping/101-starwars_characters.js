#!/usr/bin/node
/**
 * this script prints all the characters in a star war
 * movie. episode is specified by the Id
 */

const request = require('request');
const movieId = process.argv[2];
apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`

request(apiUrl, (err, response, body) => {
    if (err) {
        console.error(err);
    }
    const film = JSON.parse(body);
    film.characters.forEach(character => {
        request(character, (err, response, body) => {
            if (err) {
                console.error(err);
            }
            nameCharacter = JSON.parse(body)
            console.log(nameCharacter.name);
        });
    });
});
