const people = ["Greg", "Mary", "Devon", "James"];

// remove "Greg" from the people array

const gregIndex = people.indexOf("Greg");
if (gregIndex !== -1) {
    people.splice(gregIndex, 1);
}

// Replace "James" with "Jason"

const jamesIndex = people.indexOf("James");
if (jamesIndex !== - 1) {
    people[jamesIndex] = "Jason";
}

// Add your name to the end of the people array
people.push("Anabel");

// Log Mary's index
const maryIndex = people.indexOf("Mary");
console.log("Mary's index: ", maryIndex);

// Make a copy of the people array without "Mary" or your name
const peopleCope = people.slice(1, -1);

//  Find the index of "Foo"
const fooIndex = people.indexOf("Foo");
console.log("Index of 'Foo': ", fooIndex);

// Get the value of the last element in the array
const last = people[people.length - 1];

// Part II loops
// Iterate through the people array and console.log each person
for (const person of people) {
    console.log(person);
}

// Iterate through the people array and exit the loop after console.logging "Devon"

for (const person of people) {
    console.log(person);
    if (person === "Devon") {
        break;
    }
}

// Exercise 2: Your favorite colors
// create an array of colors
const colors = ["blue", "lavender", "white", "black"];
const suffixes = ["st", "nd", "rd", "th"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}

// Exercise 3: Repeat the question
let userInput;
do {
    userInput = parseFloat(prompt("Please enter a number:"));
} while (typeof userInput === 'number' && userInput < 10);

// Exercise 4: Building Management

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        Sarah: [3, 990],
        Dan: [4, 1000],
        David: [1, 500],
    },
}

// number of floors
console.log("Number of floors:", building.numberOfFloors);

// how many apartments are on the floors 1 and 3
console.log("Apartment on first floor:", building.numberOfAptByFloor.firstFloor);
console.log("Apartments on third floor:", building.numberOfAptByFloor.thirdFloor);

//the name of the second tenant and the number of rooms he has in his apt
// check!!!
const secondTenant = building.nameOfTenants[1];
const roomsForSecondTenant = building.numberOfRoomsAndRent[secondTenant][0];
console.log(`Second tenant: ${secondTenant}, Number of rooms: ${roomsForSecondTenant}`);

// Sarah’s and David’s rent is bigger than Dan’s rent
const sarahRent = building.numberOfRoomsAndRent.Sarah[1];
const davidRent = building.numberOfRoomsAndRent.David[1];
const danRent = building.numberOfRoomsAndRent.Dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.Dan[1] = 1200;
}

console.log("Updated rents:", building.numberOfRoomsAndRent);

// Excercise 5

const family = {
    father: "John",
    mother: "Jane",
    son: "Michael",
    daughter: "Emily",
};

// Log keys of the object
console.log("Keys of the family object:");
for (const key in family) {
    console.log(key);
}

// Log values of the object
console.log("Values of the family object:");
for (const key in family) {
    console.log(family[key]);
}

// Exercise 6
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}
// use a for loop to console log "my name is Rudolf the raindeer"
let message = '';

for (const key in details) {
    message += details[key] + ' ';
}

console.log(message.trim());

// Exercise 7: Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// Extract first letters and sort them
const firstLetters = names.map(name => name[0]).sort();

// Join the sorted letters to form the secret society's name
const secretSocietyName = firstLetters.join('');

console.log(secretSocietyName); // Output: "ABJKPS"