// import people from './data.js';

// // Function to calculate and print the average age
// function calculateAverageAge(peopleArray) {
//     const totalAge = peopleArray.reduce((sum, person) => sum + person.age, 0);
//     const averageAge = totalAge / peopleArray.length;
//     console.log(`Average Age: ${averageAge.toFixed(2)}`);
// }

// // Calculate and print the average age using the imported 'people' array
// calculateAverageAge(people);

// app.js

const fileManager = require('./filemanager.js');

// Read the content of "Hello World.txt"
fileManager.readFile('HelloWorld.txt', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }

    console.log('Content of "Hello World.txt":');
    console.log(data);

    // Write to "Bye World.txt" with the content "Writing to the file"
    fileManager.writeFile('ByeWorld.txt', 'Writing to the file', (writeErr) => {
        if (writeErr) {
            console.error('Error writing to file:', writeErr);
            return;
        }

        console.log('Successfully wrote to "Bye World.txt"');
    });
});
