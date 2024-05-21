#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const stringWrite = process.argv[3];

fs.writeFile(filePath, stringWrite, 'utf8', function (error) {
  if (error) console.log(error);
});
