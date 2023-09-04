const fs = require('fs');

// Specify the directory path you want to read
const directoryPath = './';

// Read the list of files in the specified directory
fs.readdir(directoryPath, (err, files) => {
    if (err) {
        console.error('Error reading directory:', err);
        return;
    }

    console.log('List of files in the directory:');
    files.forEach((file, index) => {
        console.log(`${index + 1}. ${file}`);
    });
});
