// Exercise 1 : Colors
// Instructions
// Using this array :

// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// // Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
// colors.forEach((color, index) => {
//     console.log(`${index + 1}# choice is ${color}.`);
// });
// // Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
// const checkViolet = colors.some((value) => value === 'Violet');
// if (checkViolet) {
//     console.log("Yeah");
// } else {
//     console.log("No...");
// }

// 🌟 Exercise 2 : Colors #2
// Instructions
// Using these arrays :

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th", "st", "nd", "rd"];
// // Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…
// // Hint : Use the array methods taught in class and ternary operator.
const colorChoices = colors.map((color, index) => {
    const suffixIndex = index === 0 ? 1 : index === 1 ? 2 : index === 2 ? 3 : 0;
    const ordinalSuffix = ordinal[suffixIndex];
    return `${index + 1}${ordinalSuffix} choice is ${color}.`;
});

// console.log(colorChoices);

// Exercise 3 : Analyzing
// Instructions
// Analyze these pieces of code before executing them. What will be the outputs ?
// ------1------
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);
//Outpout explaine --> it's spreading the array in a new array to not have one array inside other

// ------2------
// const country = "USA";
// console.log([...country]); 
//Output explained: it spread the variable of country but it turned it into an array where each letter is an element 
// ------Bonus------
// let newArray = [...[,,]];
// console.log(newArray);
//Output explained: This is unpacking an array of two empty slots


// 🌟 Exercise 4 : Employees
// Instructions
// Using this array:

// const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
// { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
// { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
// { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
// { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
// { firstName: 'Wes', lastName: 'Reid', role: 'Instructor' },
// { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor' }];
// Using the map() method, push into a new array the firstname of the user and a welcome message. You should get an array that looks like this :
// const welcomeStudents = ["Hello Bradley", "Hello Chloe", "Hello Jonathan", "Hello Michael", "Hello Robert", "Hello Wes", "Hello Zach"]

// const welcomeMessages = users.map(user => `${user.firstName}, welcome to our platform!`);

// console.log(welcomeMessages);

// 2. Using the filter() method, create a new array, containing only the Full Stack Residents.
// const fullStackResidents = users.filter(user => user.role === 'Full Stack Resident');

// console.log(fullStackResidents);

// 3. Bonus : Chain the filter method with a map method, to return an array containing only the lastName of the Full Stack Residents.

// const fullStackResidentsLastNames = users
//     .filter(user => user.role === 'Full Stack Resident')
//     .map(user => user.lastName);

// console.log(fullStackResidentsLastNames);

// 🌟 Exercise 5 : Star Wars
// Instructions
// Using this array 
// const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

// // Use the reduce() method to combine all of these into a single string.

// const singleString = epic.reduce((accumulator, currentValue) => {
//     return accumulator + ' ' + currentValue;
// });

// console.log(singleString);

// 🌟 Exercise 6 : Employees #2
// Instructions
// Using this object:

// const students = [{ name: "Ray", course: "Computer Science", isPassed: true },
// { name: "Liam", course: "Computer Science", isPassed: false },
// { name: "Jenner", course: "Information Technology", isPassed: true },
// { name: "Marco", course: "Robotics", isPassed: true },
// { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
// { name: "Jamie", course: "Big Data", isPassed: false }];
// // Using the filter() method, create a new array, containing the students that passed the course.
// // Bonus : Chain the filter method with a forEach method, to congratulate the students with their name and course name (ie. “Good job Jenner, you passed the course in Information Technology”, “Good Job Marco you passed the course in Robotics” ect…)

// const passedStudents = students.filter(student => student.isPassed);

// passedStudents.forEach(student => {
//     console.log(`Good job ${student.name}, you passed the course in ${student.course}`);
// });







