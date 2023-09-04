// const name = "Mike Tylor";

// const greeting = (name) => {
//     console.log(`Hello ${name}, welcome to NodeJS`);
// }

// greeting(name);

// usersApiModule.js

// Define the function to fetch user data

const { usersInfo } = require("./fetch.js");

// console.log(usersInfo);
// usersInfo().then(data => console.log(data));

// const info = async () => {
//     const data = await usersInfo();
//     console.log(data);
// };
// info();
(async () => {
    const data = await usersInfo();
    console.log(data);
})();
