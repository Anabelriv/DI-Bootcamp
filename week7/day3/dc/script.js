let client = "John";

const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        paid: true,
        meansOfPayment: ["cash", "creditCard"]
    }
}

// Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.
const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
}

displayGroceries();
// Create another arrow function named cloneGroceries.
const cloneGroceries = () => {
    // In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)
    let user = client;
    // Change the client variable to “Betty”. Will we also see this modification in the user variable ? Why ? --> it is still Jhon, it's inside this object and not on the global variable
    client = 'Betty';
    // In the function, create a variable named shopping that is equal to the groceries variable.
    let shopping = groceries;
    // Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ? --> it changes the value because they are a reference inside the same object
    shopping.totalPrice = 35;
    // Change the value of the paid key to false. Will we also see this modification in the shopping object ? Why ? --> yes, because it's a child of the object
    shopping.other.paid = false
    // Invoke the cloneGroceries function.


    console.log("User:", user);
    console.log("Shopping:", shopping);

}

cloneGroceries();