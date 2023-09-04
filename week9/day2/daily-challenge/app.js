// const greet = require('./greeting');

// const userName = 'John';
// const greetingMessage = greet(userName);
// console.log(greetingMessage);

import chalk from 'chalk';

// Create colorful and styled text
const colorfulMessage = chalk.bold.green('Hello, ') + chalk.underline.blue('world') + '!';

// Print the colorful message
console.log(colorfulMessage);