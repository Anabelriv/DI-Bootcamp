function areAnagrams(str1, str2) {
    // Remove whitespace and convert strings to lowercase
    const cleanStr1 = str1.replace(/\s+/g, "").toLowerCase();
    const cleanStr2 = str2.replace(/\s+/g, "").toLowerCase();

    // Convert strings to arrays, sort them, and join back to strings
    const sortedStr1 = cleanStr1.split("").sort().join("");
    const sortedStr2 = cleanStr2.split("").sort().join("");

    // Compare the sorted strings
    return sortedStr1 === sortedStr2;
}

// Test cases
console.log(areAnagrams("Astronomer", "Moon starer")); // true
console.log(areAnagrams("School master", "The classroom")); // true
console.log(areAnagrams("The Morse Code", "Here come dots")); // true
console.log(areAnagrams("Hello", "World")); // false
