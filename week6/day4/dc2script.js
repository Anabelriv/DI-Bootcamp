// daily challenge stars
const height = 6; // Adjust the height as needed

for (let i = 1; i <= height; i++) {
    let row = '';
    for (let j = 1; j <= i; j++) {
        row += '* ';
    }
    console.log(row);
}
