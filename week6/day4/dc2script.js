// daily challenge stars
const height = 6;

for (let i = 1; i <= height; i++) {
    let row = '';
    for (let j = 1; j <= i; j++) {
        row += '* ';
    }
    console.log(row);
}

const maxValue = 6;
let stars = ""
for (let i = 0; i <= maxValue; i++) {
    stars = stars + "* "
    console.log(stars);
}
