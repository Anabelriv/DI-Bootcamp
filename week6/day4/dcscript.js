// daily challenge: not bad
// create a variable called sentence
const sentence = "This is not a bad sentence";
// create a 
const wordNot = sentence.indexOf("not");
const wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    const modifiedSentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    console.log(modifiedSentence);
} else {
    console.log(sentence);
}