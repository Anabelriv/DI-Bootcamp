const fs = require('fs');

// Read the content from source.txt
fs.readFile('source.txt', 'utf8', (readErr, data) => {
    if (readErr) {
        console.error('Error reading source.txt:', readErr);
        return;
    }

    // Write the content to destination.txt
    fs.writeFile('destination.txt', data, 'utf8', (writeErr) => {
        if (writeErr) {
            console.error('Error writing to destination.txt:', writeErr);
            return;
        }

        console.log('Content copied from source.txt to destination.txt');
    });
});
