#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += char;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
