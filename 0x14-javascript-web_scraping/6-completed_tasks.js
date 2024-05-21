#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const userTasks = {};
    todos.forEach(todo => {
      if (todo.completed) {
        if (userTasks[todo.userId]) {
          userTasks[todo.userId]++;
        } else {
          userTasks[todo.userId] = 1;
        }
      }
    });
    console.log(userTasks);
  } else {
    console.log(error);
  }
});
