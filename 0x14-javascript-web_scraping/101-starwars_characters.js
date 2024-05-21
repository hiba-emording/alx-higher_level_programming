#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const APIurl = 'https://swapi-api.alx-tools.com/api/films/';

request(APIurl + movieId, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    printOrdered(characters, 0);
  } else {
    console.log(error);
  }
});

function printOrdered (characters, i) {
  if (i >= characters.length) {
    return;
  }

  request(characters[i], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      if (i + 1 < characters.length) {
        printOrdered(characters, i + 1);
      }
    } else {
      console.log(error);
    }
  });
}
