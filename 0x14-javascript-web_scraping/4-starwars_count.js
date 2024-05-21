#!/usr/bin/node

const request = require('request');
const APIurl = process.argv[2];

request(APIurl, function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body).results;
    const count = films.reduce((total, movie) => {
      const hasWedgeAntilles = movie.characters.some(character => character.endsWith('/18/'));

      if (hasWedgeAntilles) {
        return total + 1;
      } else {
        return total;
      }
    }, 0);

    console.log(count);
  } else {
    console.error('Error:', error);
  }
});
