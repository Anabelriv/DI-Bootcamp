// // const makeAllCaps = (words) => {
// //     return new Promise((resolve, reject) => {
// //         if (words.every(element) => typeof element === "string"; {
// //             const uperCaseArray = words.map(word)=>
// // return word.toUpperCase
// // resolve(uperCaseArray)
// //     } else {
// //     reject("not all strings")
// // }
// //     })
// // }

// // function sortWords(words) {
// //     return new Promise((resolve, reject) => {
// //         if (words.length > 4) {
// //             // const newArr = words.toSorted();
// //             const newArr = [...words].sort();
// //             resolve(newArr);
// //         } else {
// //             reject("There are no more than 4 words")
// //         }
// //     })
// // }

// // const arrThree = JSON.parse(JSON.stringify(arrOne))

// // makeAllCaps(["bla", "pla", "cla"])
// //     .then((arr) => console.log(arr))
// //     .then((arr) => sortWords(arr))
// //     .then((sortedarr) => console.log(sortedarr))
// //     .catch((error) => console.log("IN THE CATCH", error))


// const btn = document.querySelector("#btn");
// btn.addEventListener("click", getData)

// // function getData() {
// //     fetch("https://jsonplaceholder.typicode.com/users")
// //         .then((response) => {
// //             if (!response.ok) {
// //                 throw new Error("problem with fetch")
// //             } else {
// //                 return response.json()
// //                 //method retrieve the data and parses it
// //             }
// //         })
// //         .then((data) => {
// //             const ulElement = document.querySelector("#results")
// //             data.forEach(user => {
// //                 const liElement = document.createElement("li");
// //                 const text = document.createTextNode(`${user["name"]} - ${user["email"]}`);
// //                 liElement.appendChild(text);
// //                 ulElement.appendChild(liElement)
// //             });
// //         })
// //         .catch((error) => console.log("IN THE CATCH", error))
// // }

// function getData() {
//     fetch('https://api.chucknorris.io/jokes/random')
//         .then((response) => {
//             if (!response.ok) {
//                 throw new Error("Problem with fetch")
//             } else {
//                 return response.json();
//             }
//         })
//         .then((data) => {
//             const pElement = document.querySelector("#results");
//             const text = document.createTextNode(`${data["value"]}`);
//             pElement.appendChild(text);
//         })
//         .catch((error) => console.log("IN THE CATCH", error));
// }

// function check() {
//     return new Promise((resolve, reject) => {
//         if (condition) {
//             resolve()
//         } else {
//             reject()
//         }
//     })
// }

async function getData() {
    try {
        const response = await fetch("https://api.chucknorris.io/jokes/random")
        if (!response.ok) {
            throw new Error("Problem with fetch")
        } else {
            const data = await response.json();
            const pElement = document.querySelector("#results");
            const text = document.createTextNode(`${data["value"]}`);
            pElement.appendChild(text);
        }
    } catch (err) {
        console.log("In the catch", err)
    }
}
