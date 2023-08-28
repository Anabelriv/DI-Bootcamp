const form = document.getElementById('myForm');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const lastName = document.getElementById('lastName').value;

    const formData = {
        name: name,
        lastName: lastName
    };

    const formDataString = JSON.stringify(formData);

    resultDiv.textContent = formDataString;
});