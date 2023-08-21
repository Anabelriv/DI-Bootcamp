// Exercise 1 : Find The Numbers Divisible By 23
// Instructions
// Create a function call displayNumbersDivisible() that takes no parameter.

function displayNumbersDivisible() {
    let sum = 0;
    // In the function, loop through numbers 0 to 500.
    for (let i = 0; i <= 500; i++) {
        if (i % 23 === 0) {
            console.log(i);
            sum += i;
        }
    }
    // At the end, console.log the sum of all numbers that are divisible by 23.
    console.log("Sum of numbers divisible by 23:", sum);
}

//displayNumbersDivisible();

// Console.log all the numbers divisible by 23.
//console.log.displayNumbersDivisible()

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 
// 368 391 414 437 460 483
// Sum : 5313


// 🌟 Exercise 2 : Shopping List
// Instructions
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
const shoppingList = {
    "banana": 1,
    "orange": 1,
    "apple": 1
};

const price = {
    "banana": 0.5,
    "orange": 0.75,
    "apple": 1.0
};
// Create a function called myBill() that takes no parameters.

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
function myBill() {
    let totalPrice = 0;

    for (const item in shoppingList) {
        if (item in price) {
            totalPrice += shoppingList[item] * price[item];
        }
    }

    return totalPrice;
}
// Call the myBill() function.

const totalBill = myBill();
console.log("Total Bill:", totalBill);
// Bonus: If the item is in stock, decrease the item’s stock by 1


// Exercise 3 : What’s In My Wallet ?
// Instructions


// In the function, determine whether or not you can afford the item.


// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01


function changeEnough(itemPrice, amountOfChange) {
    const quartersValue = 0.25;
    const dimesValue = 0.10;
    const nickelsValue = 0.05;
    const penniesValue = 0.01;

    const totalChange = (amountOfChange[0] * quartersValue) +
        (amountOfChange[1] * dimesValue) +
        (amountOfChange[2] * nickelsValue) +
        (amountOfChange[3] * penniesValue);
    // If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
    // If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

    return totalChange >= itemPrice;
}
// After you created the function, invoke it like this:
// Examples
console.log(changeEnough(4.25, [25, 20, 5, 0])); // Should return true
console.log(changeEnough(14.11, [2, 100, 0, 0])); // Should return false
console.log(changeEnough(0.75, [0, 0, 20, 5])); // Should return true


// 🌟 Exercise 4 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
// Define a function for calculating hotel cost
function hotelCost() {
    let numberOfNights;
    do {
        numberOfNights = prompt("How many nights do you want to stay in the hotel?");
    } while (!Number.isInteger(Number(numberOfNights)));

    return 140 * parseInt(numberOfNights);
}
// hotelCost();
// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

function planeRideCost() {
    let destination;
    do {
        destination = prompt("Where would you like to go (London, Paris, or other)?");
    } while (typeof destination !== "string");

    switch (destination.toLowerCase()) {
        case "london":
            return 183;
        case "paris":
            return 220;
        default:
            return 300;
    }
}
// planeRideCost();
// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.
function rentalCarCost() {
    let numberOfDays;
    do {
        numberOfDays = prompt("How many days would you like to rent the car?");
    } while (!Number.isInteger(Number(numberOfDays)));

    let cost = 40 * parseInt(numberOfDays);
    if (parseInt(numberOfDays) > 10) {
        cost *= 0.95; // Apply 5% discount
    }
    return cost;
}
// rentalCarCost();
// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()

// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.
function totalVacationCost() {
    const hotel = hotelCost();
    const plane = planeRideCost();
    const car = rentalCarCost();

    const totalCost = hotel + plane + car;
    return totalCost;
}

// totalVacationCost();

// 🌟 Exercise 5 : Users
// Using Javascript:
// Retrieve the div and console.log it
const containerDiv = document.getElementById('container');
console.log(containerDiv);
// Change the name “Pete” to “Richard”.
const peteElement = document.querySelector('.list:nth-child(1) li:nth-child(2)');
peteElement.textContent = "Richard";

// Delete the second <li> of the second <ul>.
const secondUl = document.querySelectorAll('.list:nth-child(2) li')[1];
secondUl.remove();
// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)
const listItems = document.querySelectorAll('.list li');
listItems.forEach(item => {
    item.textContent = "Your Name";
});
// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
const ulElements = document.querySelectorAll('.list');
ulElements.forEach(ul => {
    ul.classList.add('student_list');
});
// Add the classes university and attendance to the first <ul>.
ulElements[0].classList.add('university', 'attendance');

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.

// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
const danLi = document.querySelector('.list:first-child li:last-child');
danLi.style.display = 'none';
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
const richardLi = document.querySelector('.list:first-child li:nth-child(2)');
richardLi.style.border = '1px solid black'
// Change the font size of the whole body.
document.body.style.fontSize = '16px';
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).


// 🌟 Exercise 6 : Change The Navbar
// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>



// Add the code above, to your HTML file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).


// Exercise 7 : My Book List
// Instructions
// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.
