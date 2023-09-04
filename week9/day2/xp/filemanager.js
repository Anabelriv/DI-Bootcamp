// fileManager.js

const fs = require('fs');

// Function to read a file
function readFile(fileName, callback) {
    fs.readFile(fileName, 'utf8', (err, data) => {
        if (err) {
            callback(err, null);
            return;
        }
        callback(null, data);
    });
}

// Function to write to a file
function writeFile(fileName, content, callback) {
    fs.writeFile(fileName, content, 'utf8', (err) => {
        if (err) {
            callback(err);
            return;
        }
        callback(null);
    });
}

module.exports = { readFile, writeFile };
