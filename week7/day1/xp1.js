// Change the id attribute value using setAttribute
const navBar = document.getElementById('navBar');
navBar.setAttribute('id', 'socialNetworkNavigation');

// Create a new <li> element and append it to the <ul>
const newLi = document.createElement('li');
const logoutText = document.createTextNode('Logout');
newLi.appendChild(logoutText);

const ul = navBar.querySelector('ul');
ul.appendChild(newLi);

// Retrieve and display text content of first and last <li> elements
const firstLi = ul.firstElementChild;
const lastLi = ul.lastElementChild;

console.log('Text of first link:', firstLi.textContent);
console.log('Text of last link:', lastLi.textContent);
