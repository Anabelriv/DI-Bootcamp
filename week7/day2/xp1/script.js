// Retrieve <h1> DOM property

const h1Element = document.querySelector('h1');
console.log(h1Element);

// Remove the last paragraph

const article = document.querySelector('article');
const paragraphs = article.querySelectorAll('p');
if (paragraphs.length > 0) {
    const lastParagraph = paragraphs[paragraphs.length - 1];
    article.removeChild(lastParagraph);
}

// change the color of the background
const h2Element = document.querySelector('h2');
h2Element.addEventListener('click', function () {
    h2Element.style.backgroundColor = 'red';
});

// hide <h3> 
const h3Element = document.querySelector('h3');
h3Element.addEventListener('click', function () {
    h3Element.style.display = 'none';
});

// button

const boldButton = document.getElementById('boldButton');
const allParagraphs = document.querySelectorAll('p');

boldButton.addEventListener('click', function () {
    allParagraphs.forEach(paragraph => {
        paragraph.style.fontWeight = 'bold';
    });
});

// Exercise 2 Forms
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const usersAnswerList = document.querySelector('.usersAnswer');

    // Retrieve the form and console.log it
    console.log(form);

    // Retrieve the inputs by their id and console.log them
    const fnameInput = document.getElementById('fname');
    const lnameInput = document.getElementById('lname');
    console.log(fnameInput, lnameInput);

    // Retrieve the inputs by their name attribute and console.log them
    const firstnameInput = document.querySelector('input[name="firstname"]');
    const lastnameInput = document.querySelector('input[name="lastname"]');
    console.log(firstnameInput, lastnameInput);

    // Form submit event listener
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Get input values and validate if not empty
        const firstName = fnameInput.value.trim();
        const lastName = lnameInput.value.trim();

        if (firstName !== '' && lastName !== '') {
            // Create li elements for input values
            const firstNameLi = document.createElement('li');
            firstNameLi.textContent = firstName;
            const lastNameLi = document.createElement('li');
            lastNameLi.textContent = lastName;

            // Append li elements to the ul
            usersAnswerList.appendChild(firstNameLi);
            usersAnswerList.appendChild(lastNameLi);

            // Clear input values
            fnameInput.value = '';
            lnameInput.value = '';
        }
    });
});
// Exercise 3
// Declare a global variable named allBoldItems
let allBoldItems;

// Function to collect all bold items inside the paragraph
function getBoldItems() {
    const paragraph = document.querySelector('p');
    allBoldItems = paragraph.querySelectorAll('strong');
}

// Function to change the color of all bold text to blue
function highlight() {
    allBoldItems.forEach(item => {
        item.style.color = 'blue';
    });
}

// Function to change the color of all bold text back to black
function returnItemsToDefault() {
    allBoldItems.forEach(item => {
        item.style.color = 'black';
    });
}

// Add event listeners for mouseover and mouseout
document.addEventListener('DOMContentLoaded', function () {
    getBoldItems();

    const paragraph = document.querySelector('p');
    paragraph.addEventListener('mouseover', highlight);
    paragraph.addEventListener('mouseout', returnItemsToDefault);
});

// Exercise 4

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('MyForm');
    const radiusInput = document.getElementById('radius');
    const volumeInput = document.getElementById('volume');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        const radius = parseFloat(radiusInput.value);
        if (!isNaN(radius)) {
            const volume = calculateVolume(radius);
            volumeInput.value = volume.toFixed(2);
        }
    });
});

// Function to calculate the volume of a sphere
function calculateVolume(radius) {
    const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
    return volume;
}

// Exercise 5: Event Listeners
document.addEventListener('DOMContentLoaded', function () {
    const element = document.getElementById('element');

    // Click event listener to change background color
    element.addEventListener('click', function () {
        const randomColor = getRandomColor();
        element.style.backgroundColor = randomColor;
    });

    // Mouseover event listener to change position on X-axis
    element.addEventListener('mouseover', function () {
        element.style.left = Math.random() * window.innerWidth + 'px';
    });

    // Mouseout event listener to change position on Y-axis
    element.addEventListener('mouseout', function () {
        element.style.top = Math.random() * window.innerHeight + 'px';
    });

    // Double click event listener to change font size
    element.addEventListener('dblclick', function () {
        const randomSize = Math.floor(Math.random() * 40 + 10) + 'px';
        element.style.fontSize = randomSize;
    });
});

// Function to generate a random color
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
