// 🌟 Exercise 1 : Location
// Instructions
// Analyze the code below. What will be the output?
const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const { name, location: { country, city, coordinates: [lat, lng] } } = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);
// Output: "I am John Doe from Vancouver, Canada. Latitude 49.2827,Longitud -123.1207 " -- It deconstructed from the object 

// 🌟 Exercise 2: Display Student Info
// Instructions
function displayStudentInfo(objUser) {
    //destructuring
    const { first, last } = objUser;
    const output = `Your full name is ${first} ${last}`;
    return output;
}

displayStudentInfo({ first: 'Elie', last: 'Schoppik' });


// Using the code above, destructure the parameter inside the function and return a string as the example seen below:
// //output : 'Your full name is Elie Schoppik'
const studentInfo = displayStudentInfo({ first: 'Elie', last: 'Schoppik' });

console.log(studentInfo);

// 🌟 Exercise 3: User & Id
// Instructions
// Using this object 
const users = { user1: 18273, user2: 92833, user3: 90315 }

// Using methods taught in class, turn the users object into an array:
// Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
// FYI : The number is their ID number.
const usersArray = Object.entries(users);
console.log(usersArray);
// Modify the outcome of part 1, by multipling the user’s ID by 2.
// Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] 
const modifiedUsersArray = usersArray.map(([user, id]) => [user, id * 2]);
console.log(modifiedUsersArray);


// Exercise 4 : Person Class
// Instructions
// Analyze the code below. What will be the output?
class Person {
    constructor(name) {
        this.name = name;
    }
}

const member = new Person('John');
console.log(typeof member);

// Output: object, John is an instance of the object

// 🌟 Exercise 5 : Dog Class
// Instructions
// Using the Dog class below:

class Dog {
    constructor(name) {
        this.name = name;
    }
};
// Analyze the options below. Which constructor will successfully extend the Dog class?
//   // 1
class Labrador extends Dog {
    constructor(name, size) {
        this.size = size;
    }
};


//   // 2
class Labrador extends Dog {
    constructor(name, size) {
        super(name);
        this.size = size;
    }
};


// 3
class Labrador extends Dog {
    constructor(size) {
        super(name);
        this.size = size;
    }
};


//   // 4
class Labrador extends Dog {
    constructor(name, size) {
        this.name = name;
        this.size = size;
    }
};

// The right one is option 2 because it's expecting from the class the argument of name so we use super, after that we are adding another parameter of size. 

// 🌟 Exercise 6 : Challenges
// Evaluate these (ie True or False)

// [2] === [2] 
// {} === {}
// Output: they are both false because they are in a different place in memory

// What is, for each object below, the value of the property number and why?

// const object1 = { number: 5 }; 
// const object2 = object1; 
// const object3 = object2; 
// const object4 = { number: 5};

// object1.number = 4;
// console.log(object2.number) // output number:4 --> point to the same object in memory as object 1
// console.log(object3.number) // output number:4 --> point to the same object in memory as object 2 and object 1
// console.log(object4.number)// output number:5 --> new space in memory


// Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin ect …

// Create a class Mamal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes.

// Create a farmerCow object that is an instance of the class Mamal. The object accepts a name, a type and a color and calls the sound method that “moos” her information.
// For example: Moooo I'm a cow, named Lily and I'm brown and white

class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

class Mamal extends Animal {
    sound(animalSound) {
        return `The ${this.type} named ${this.name} is ${this.color} and makes a ${animalSound} sound.`;
    }
}

class FarmerCow extends Mamal {
    constructor(name, color) {
        super(name, "cow", color);
    }

    sound() {
        return super.sound("moos");
    }
}

const farmerCow = new FarmerCow("Lily", "brown and white");
const cowSound = farmerCow.sound();
console.log(cowSound);
