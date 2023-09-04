// Require the lodash package
const lodash = require('lodash');

// Require the custom math module
const math = require('./math.js');

// Perform calculations using lodash and the custom math module
const numbers = [1, 2, 3, 4, 5];

const sum = lodash.sum(numbers); // Using lodash to calculate the sum
const product = math.multiply(3, 4); // Using the custom math module to calculate the product

console.log(`Sum of numbers: ${sum}`);
console.log(`Product of 3 and 4: ${product}`);
