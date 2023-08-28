// Instructions
// 1rst Daily Challenge
// Create two functions. Each function should return a promise.
// The first function called makeAllCaps(), takes an array of words as an argument
// If all the words in the array are strings, resolve the promise. The value of the resolved promise is the array of words uppercased.
// else, reject the promise with a reason.
function makeAllCaps(words) {
    return new Promise((resolve, reject) => {
        if (typeof words === 'object' && Array.isArray(words)) {
            const upperCaseWords = words.map(word => {
                if (typeof word === 'string') {
                    return word.toUpperCase();
                } else {
                    reject("Not a string");
                }
            });
            resolve(upperCaseWords);
        } else {
            reject("Not an array");
        }
    });
}
// The second function called sortWords(), takes an array of words uppercased as an argument
// If the array length is bigger than 4, resolve the promise. The value of the resolved promise is the array of words sorted in alphabetical order.
// else, reject the promise with a reason.
function sortWords(words) {
    return new Promise((resolve, reject) => {
        if (words.length > 4) {
            resolve(words.sort());
        } else {
            reject("There are no more than 4 words")
        }
    })
}

// Test:

// //in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

// //in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

// //in this example, you should see in the console, 
// // the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
    .catch(error => console.log(error))


// Output:

// output


// 2nd Daily Challenge
// const morse = `{
//   "0": "-----",
//   "1": ".----",
//   "2": "..---",
//   "3": "...--",
//   "4": "....-",
//   "5": ".....",
//   "6": "-....",
//   "7": "--...",
//   "8": "---..",
//   "9": "----.",
//   "a": ".-",
//   "b": "-...",
//   "c": "-.-.",
//   "d": "-..",
//   "e": ".",
//   "f": "..-.",
//   "g": "--.",
//   "h": "....",
//   "i": "..",
//   "j": ".---",
//   "k": "-.-",
//   "l": ".-..",
//   "m": "--",
//   "n": "-.",
//   "o": "---",
//   "p": ".--.",
//   "q": "--.-",
//   "r": ".-.",
//   "s": "...",
//   "t": "-",
//   "u": "..-",
//   "v": "...-",
//   "w": ".--",
//   "x": "-..-",
//   "y": "-.--",
//   "z": "--..",
//   ".": ".-.-.-",
//   ",": "--..--",
//   "?": "..--..",
//   "!": "-.-.--",
//   "-": "-....-",
//   "/": "-..-.",
//   "@": ".--.-.",
//   "(": "-.--.",
//   ")": "-.--.-"
// }`
// Create three functions. The two first functions should return a promise..

// The first function is named toJs():
// this function converts the morse json string provided above to a morse javascript object.
// if the morse javascript object is empty, throw an error (use reject)
// else return the morse javascript object (use resolve)

function toJs() {
    return new Promise((resolve, reject) => {
        try {
            const morseJS = JSON.parse(morse);
            if (Object.keys(morseJS).length === 0) {
                reject("Morse object is empty")
            } else {
                resolve(morseJS);
            }
        } catch (error) {
            reject("Error parsing morse JSON")
        }
    });
}
// The second function called toMorse(morseJS), takes one argument: the new morse javascript object.

// This function asks the user for a word or a sentence.
// if the user entered a character that doesn’t exist in the new morse javascript object, throw an error. (use reject)
// else return an array with the morse translation of the user’s word.
// if the user enters the word "Hello", the promise resolves with this value ["....", ".", ".-..", ".-..","---"]
// if the user entered the word "¡Hola!", the promise rejects because the character "¡" doesn't exist in the morse javascript object
function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
        const userInput = prompt("Enter a word or sentence:");
        if (!userInput) {
            reject("No input provided");
            return;
        }

        const morseTranslation = [];
        for (const char of userInput) {
            const morseCode = morseJS[char.toLowerCase()];
            if (!morseCode) {
                reject(`Character "${char}" doesn't exist in morse code`);
                return;
            }
            morseTranslation.push(morseCode);
        }
        resolve(morseTranslation);
    });
}

// The third function called joinWords(morseTranslation), takes one argument: the morse translation array

// this function joins the morse translation by using line break and display it on the page (ie. On the DOM)
function joinWords(morseTranslation) {
    const morseString = morseTranslation.join("\n");
    console.log(morseString);
}


// Chain the three functions.
// Example:
// "Hello" gives you
// ....
// .
// .-..
// .-..
// ---
toJs()
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.error(error));