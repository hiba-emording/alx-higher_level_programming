#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function (error, data) {
  if (error) {
    const formattedError = `{ Error: ${error.message}\n    at ${error.stack.split('\n')[1]}\n  errno: ${error.errno},\n  code: '${error.code}',\n  syscall: '${error.syscall}',\n  path: '${error.path}' }`;
    console.error(formattedError);
  } else {
    console.log(data);
  }
});
