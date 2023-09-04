// const greeting = require('./greeting.js');

// console.log("greeting =>", greeting("Mary"));
// console.log(greeting.hello("dan"));

const { hello, greeting } = require("./greeting.js");
console.log(hello('dan'), greeting('Mary'));
