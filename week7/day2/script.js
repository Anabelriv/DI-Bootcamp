// function clicked() {
//     alert("Button was clicked")
// }

// const button = document.getElementById('clickEvent')

// button.addEventListener("click", clicked);

// function mouseOver() {
//     console.log("mouse over event fired")
// }
// button.onmouseover = mouseOver

// let row = 1;
// function insertRow() {
//     row++;
//     // Get the table element
//     const table = document.getElementById('sampleTable');

//     // Create a new row and cells
//     const newRow = table.insertRow();

//     const cell1 = newRow.insertCell(0);
//     const cell2 = newRow.insertCell(1);

//     // Set content for the new cells
//     cell1.innerHTML = `Row ${row} cell 1`;
//     cell2.innerHTML = `Row ${row} cell 2`;
// }

// document.addEventListener('DOMContentLoaded', function () {
//     const jsStyleButton = document.getElementById('jsstyle');

//     jsStyleButton.addEventListener('click', function () {
//         jsStyleButton.style.backgroundColor = 'blue';
//         jsStyleButton.style.color = 'white';
//         jsStyleButton.style.border = 'none';
//     });

//     jsStyleButton.addEventListener('mouseover', function () {
//         jsStyleButton.style.cursor = 'pointer';
//         jsStyleButton.style.backgroundColor = 'lightblue';
//     });

//     jsStyleButton.addEventListener('mouseout', function () {
//         jsStyleButton.style.backgroundColor = '';
//     });
// });

function getValue() {
    // event.preventDefault();
    // console.log(event.target.elements);
    const firstName = document.forms["form1"]["fname"].value;
    const lastName = document.forms["form1"]["lname"].value;

    alert(`First Name: ${firstName}\nLast Name: ${lastName}`);
}
console.log(getValue());

