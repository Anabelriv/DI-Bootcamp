const grade = 80
const myPromise = new Promise((resolve, reject) => {
    if (grade > 75) {
        resolve("Computer")
    } else {
        reject("Nothing")
    }
});

myPromise.then((giftFromMum) => {
    console.log("in the first then", giftFromMum);
})
    .then((result) => {
        console.log("in the second then", result);
    })
    .catch((error) => {
        console.log("in the catch, the error is", error);
    })

// Create a function that takes in a single parameter and returns a new promise.
// Using setTimeout, after 5000 milliseconds, the promise will either resolve or reject.
// If the input is a string, the promise resolves with that same string uppercased.
// If the input is anything but a string it rejects with that same input.
// Use then to repeat the string twice use catch to console.log the error finally call a function that console.log ("congratulation")
function processInput(valueInput) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (typeof valueInput === String) {
                resolve(valueInput.toUpperCase());
            } else {
                reject("Not a string", valueInput);
            }
        }, 5000);
    });
}
processInput("hello")
    .then(result => {
        console.log((result + " ").repeat(2).trim());
    })
    .catch(error => {
        console.log(error);
    })
    .finally(() => {
        console.log("Congratulations");
    });

processInput(123)
    .then(result => {
        console.log((result + " ").repeat(2).trim());
    })
    .catch(error => {
        console.log(error);
    })
    .finally(() => {
        console.log("Congratulations");
    });