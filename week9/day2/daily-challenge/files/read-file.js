const fs = require('fs');

function readFileContent() {
    fs.readFile('file-data.txt', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading the file:', err);
            return;
        }

        console.log('File content:');
        console.log(data);
    });
}

module.exports = readFileContent;
