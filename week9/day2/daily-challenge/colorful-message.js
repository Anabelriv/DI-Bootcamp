// import chalk from 'chalk';
const colorfulMessage = require('chalk');
// Create colorful and styled text
const colorfulMessage = chalk.bold.green('Hello, ') + chalk.underline.blue('world') + '!';

// Print the colorful message
console.log(colorfulMessage);
module.exports = colorfulMessage;