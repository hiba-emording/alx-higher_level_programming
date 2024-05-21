#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const APIurl = 'https://swapi-api.alx-tools.com/api/films/';

request.get(APIurl + movieId, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.log(error);
        }
      });
    });
  } else {
    console.log(error);
  }
});
