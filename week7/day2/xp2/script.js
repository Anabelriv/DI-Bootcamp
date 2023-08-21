// Exercise 1 Timer
// Part I
setTimeout(function () {
    alert("Hello World");
}, 2000);
// Part II
setTimeout(function () {
    const container = document.getElementById('container');
    const newParagraph = document.createElement('p');
    newParagraph.textContent = "Hello World";
    container.appendChild(newParagraph);
}, 2000);
// Part III
let paragraphCount = 0;
const interval = setInterval(function () {
    const container = document.getElementById('container');
    const newParagraph = document.createElement('p');
    newParagraph.textContent = "Hello World";
    container.appendChild(newParagraph);

    paragraphCount++;

    if (paragraphCount >= 5) {
        clearInterval(interval);
    }
}, 2000);

// Clear interval when the button is clicked
const clearButton = document.getElementById('clear');
clearButton.addEventListener('click', function () {
    clearInterval(interval);
});

// Exercise 2 
function myMove() {
    const container = document.getElementById('container');
    const animate = document.getElementById('animate');

    let position = 0;
    const interval = setInterval(frame, 1);

    function frame() {
        if (position >= container.offsetWidth - animate.offsetWidth) {
            clearInterval(interval);
        } else {
            position++;
            animate.style.left = position + 'px';
        }
    }
}
