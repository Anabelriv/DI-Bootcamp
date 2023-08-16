console.log("Hello World");
// variables
let addressNumber = 3;
let addressStreet = "Hagana";
let country = "Israel";
// let myName = "anabel";
globalAddress = (addressNumber + " " + addressStreet + " " + country);
console.log("I live in " + globalAddress)
// Undefined

let a;
console.log(a);

// Strings
let exampleString = "Hello";
let exampleString2 = "World";
console.log(exampleString + " " + exampleString2);

let longString = "This is a very long \nstring which needs to wrap across multiple lines \nhi bla bla";
console.log(longString);

// let myName = "ble bla bla";
// console.log(myName.length);

//  Indexof
// console.log(myName.indexOf());

// Number
//  inNan
// let op = "2"
// console.log(isNan(op));
// console.log(op.toString());
// Comparison
// compare value and type
// console.log(1 === 1);
// let x = 6;
// x++;
// console.log("before alert");
// alert("Welcome to my website");
// console.log("after Alert");

// let userAnaswer = prompt("What is your name?", "Guest");
// console.log("Welcome to the website " + userAnaswer);

// Arrays
// let users = ["Anabel", "Daniel"];
// let y = "1";
// console.log(typeof users);

// let arrayCeption = [
//     [1, 2, 3],
//     [5, 6, 7, 8]
// ];
// console.log(arrayCeption[0][1]);

// splice
// let colors = ["green", "pink", "green", "blue"]
// console.log(colors);
// colors.splice(1, 2);
// console.log(colors);

// Create an array called 'pets'
// var pets = ['cat', 'dog', 'fish', 'rabbit', 'cow'];

// Display 'dog'
// console.log(pets[1]); // Output: dog

// Add 'horse' to the array and remove 'rabbit'
// pets.push('horse');
// pets.splice(3, 1);

// Display the array length
// console.log(pets.length); // Output: 5

let x = 18

if (x >= 21) {
    console.log("You can drink in the US")
} else if (x === 18) {
    console.log("You can drink in most places excluding the US")
}
else if (x >= 16 && x < 18) {
    "You can drink in germany"
}
else {
    console.log("you are too young to drink in the US")
}