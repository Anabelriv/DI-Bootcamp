// Require the products.js module
const products = require('./products.js');

// Function to search for a product by name
function findProductByName(productName) {
    const product = products.find((item) => item.name === productName);
    return product;
}

//test
console.log("Searching for product: Laptop");
const laptop = findProductByName("Laptop");
if (laptop) {
    console.log("Product found:");
    console.log("Name:", laptop.name);
    console.log("Price:", laptop.price);
    console.log("Category:", laptop.category);
} else {
    console.log("Product not found.");
}

console.log("\nSearching for product: T-shirt");
const tShirt = findProductByName("T-shirt");
if (tShirt) {
    console.log("Product found:");
    console.log("Name:", tShirt.name);
    console.log("Price:", tShirt.price);
    console.log("Category:", tShirt.category);
} else {
    console.log("Product not found.");
}

