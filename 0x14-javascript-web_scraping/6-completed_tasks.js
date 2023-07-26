#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);
      let completedTask = {};
      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTask[todo.userId] === undefined) {            completedTask[todo.userId] = 1;
          } else {
            completedTask[todo.userId] += 1;
          }
        }
      });
      console.log(completedTask);
    } catch (e) {
      console.error('Error: Unable to parse data from the API response as JSON.');
    }
  } else {
    console.error('Error: Unable to fetch data from the API.');
  }
});
