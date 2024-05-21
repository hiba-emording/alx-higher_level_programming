#!/usr/bin/node

const request = require('request');
const urlRequest = process.argv[2];

request.get(urlRequest).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
