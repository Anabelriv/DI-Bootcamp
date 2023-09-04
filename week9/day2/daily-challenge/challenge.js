// app.js
const greet = require('./greeting');
const displayColorfulMessage = require('./colorful-message');
const readFileContent = require('./read-file');

const userName = 'John';
const greetingMessage = greet(userName);
console.log(greetingMessage);

displayColorfulMessage();

readFileContent();
