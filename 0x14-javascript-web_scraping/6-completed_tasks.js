#!/usr/bin/node
/**
 * this script extracts from an api the number of tasks
 * completed by a user via the user id
 */

const request = require('request');

const apiUrl = process.argv[2];
if (!apiUrl) {
  console.error('Usage: 6-completed_tasks.js <url>');
  process.exit(1);
}

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const todoCompleted = {};
    todos.forEach(todo => {
      if (todo.completed) {
        if (todoCompleted[todo.userId]) {
          todoCompleted[todo.userId] += 1;
        } else {
          todoCompleted[todo.userId] = 1;
        }
      }
    });
    console.log(todoCompleted);
  }
});
