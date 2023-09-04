const fs = require("fs");
// const data = fs.readFileSync("users.json", "utf-8");
// console.log(data);

// const data = fs.readFile("users.json", "utf-8", (err, data) => {
//     if (err) return console.log(err);
//     console.log(data);
// });
// console.log(data);
let arr = [{ username: "aaa", password: 123456 }];

fs.writeFile('info', JSON.stringify(arr), (err) => {
    if (err) return console.log(err);
});