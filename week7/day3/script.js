// // Exercise 1
// // Predictions
// // #1
// // function funcOne() {
// //     let a = 5;
// //     if (a > 1) {
// //         a = 3;
// //     }
// //     alert(`inside the funcOne function ${a}`);
// // }

// // #1.1 - run in the console:
// // funcOne() // -->  here "a" will equal to 3 because I am checking if a is smaller than 5 then give the value to 3
// // #1.2 What will happen if the variable is declared 
// // with const instead of let ? --> this will be an error, can't change the value of const

// //#2
// // let a = 0;
// // function funcTwo() {
// //     a = 5;
// // }

// // function funcThree() {
// //     alert(`inside the funcThree function ${a}`);
// // }

// // #2.1 - run in the console:
// // funcThree()
// // funcTwo()
// // funcThree()
// // #2.2 What will happen if the variable is declared --> it will return the value declared outside of the function if it was given before the function, in this case 0 , for funTwo it will return five and again 5
// // with const instead of let ? --> error can't change the value 


// //#3
// // function funcFour() {
// //     window.a = "hello";
// // }


// // function funcFive() {
// //     alert(`inside the funcFive function ${a}`);
// // }

// // #3.1 - run in the console:
// // funcFour() //--> returns undefined, wrong hierarchie, after window we have Document, we don't have an element called a in Window
// // funcFive() // --> returns 5, it takes the changes done to a

// //#4
// // let a = 1;
// // function funcSix() {
// //     let a = "test";
// //     alert(`inside the funcSix function ${a}`);
// // }


// // // #4.1 - run in the console:
// // funcSix() //--> returns the string test
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ? --> error

// //#5
// // let a = 2;
// // if (true) {
// //     let a = 5;
// //     alert(`in the if block ${a}`);
// // }
// // alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared --> returns 5 because it is inside the if statement, outside the if block it will return 2 
// // with const instead of let ? --> returns error can't change a 

// 🌟 Exercise 2 : Ternary Operator
// Instructions
// Using the code below:

// function winBattle() {
//     return true;
// }
// Transform the winBattle() function to an arrow function.
// const winBattle = () => { True }
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
//const experiencePoints = winBattle() ? 10 : 1;

// Console.log the experiencePoints variable.

//console.log(experiencePoints);

// 🌟 Exercise 3 : Is It A String ?
// Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
// Check out the example below to see the expected output
// Example:
const isString = value => typeof value === 'string';

console.log(isString('hello'));
// //true
console.log(isString([1, 2, 4, 0]));
// //false


// 🌟 Exercise 4 : Find The Sum
// Instructions
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.
const sum = (x, y) => x + y;
console.log(sum(3, 4))

// 🌟 Exercise 5 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)
function kgToGramsDeclaration(weightInKg) {
    return weightInKg * 1000;
}


// First, use function declaration and invoke it.
console.log(kgToGramsDeclaration(2.5)); // Output: 2500
// Then, use function expression and invoke it.
// Function Expression
const kgToGramsExpression = function (weightInKg) {
    return weightInKg * 1000;
};

// Invoking the function
console.log(kgToGramsExpression(2.5)); // Output: 2500

// Write in a one line comment, the difference between function declaration and function expression.-->  function declarations can be used before they are declared, and function expressions can only be used after they are defined.
// Finally, use a one line arrow function and invoke it.
// Arrow Function
const kgToGramsArrow = weightInKg => weightInKg * 1000;

// Invoking the function
console.log(kgToGramsArrow(2.5)); // Output: 2500


// 🌟 Exercise 6 : Fortune Teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

(function (numberOfChildren, partnerName, location, jobTitle) {
    const fortune = `You will be a ${jobTitle} in ${location}, and married to ${partnerName} with ${numberOfChildren} kids.`;
    document.getElementById('fortune').textContent = fortune;
})(3, "Alice", "New York", "Software Engineer");

// 🌟 Exercise 7 : Welcome
// Instructions
// John has just signed in to your website and you want to welcome him.

// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.

(function (userName) {
    const navbar = document.getElementById('navbar');

    const userDiv = document.createElement('div');
    userDiv.classList.add('user-profile');

    // Add user's name
    const userNameElement = document.createElement('p');
    userNameElement.textContent = `Welcome, ${userName}!`;
    userDiv.appendChild(userNameElement);

    const userProfilePic = document.createElement('img');
    userProfilePic.src = 'profile.jpg';
    userProfilePic.alt = `${userName}'s Profile Picture`;
    userDiv.appendChild(userProfilePic);
    navbar.appendChild(userDiv);
})("John");

// 🌟 Exercise 8 : Juice Bar
// Instructions
// You will use nested functions, to open a new juice bar.

// Part I:
// The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.

// The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

// Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.

// Part I
function makeJuice(size) {
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        const juiceSentence = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}`;
        console.log(juiceSentence);
    }
    addIngredients("apple", "orange", "carrot");
}

makeJuice("medium"); // Output: The client wants a medium juice, containing apple, orange, carrot

// Part II:
// In the makeJuice function, create an empty array named ingredients.

// The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.

// Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

// The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.

// Part II
function makeJuice(size) {
    //create an empty array named ingredients.
    const ingredients = [];
    // addIngredients function should now receive 3 ingredients, and push them into the ingredients array.
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }

    addIngredients("apple", "orange", "carrot");
    addIngredients("strawberry", "banana", "pineapple");

    function displayJuice() {
        const juiceSentence = `The client wants a ${size} juice, containing ${ingredients.join(", ")}`;
        console.log(juiceSentence);
    }

    displayJuice();
}

makeJuice("large");
