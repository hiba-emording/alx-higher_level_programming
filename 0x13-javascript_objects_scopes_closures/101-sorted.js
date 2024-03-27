#!/usr/bin/node
const data = require('./101-data').dict;

const entries = Object.entries(data);
const values = Object.values(data);
const uniqueValues = [...new Set(values)];
const newData = {};

for (const value of uniqueValues) {
  const keyList = [];
  for (const entry of entries) {
    if (entry[1] === value) {
      keyList.unshift(entry[0]);
    }
  }
  newData[value] = keyList;
}

console.log(newData);
