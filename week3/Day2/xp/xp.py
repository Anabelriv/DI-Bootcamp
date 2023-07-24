# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    


bengal_cat = Bengal("Bengal Cat", 3)
chartreux_cat = Chartreux("Chartreux Cat", 4)
siamese_cat = Siamese("Siamese Cat", 2)


# Create a list called all_cats with the three cat instances
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Create an instance of the Pets class with the list of all_cats
sara_pets = Pets(all_cats)

# Take all the cats for a walk
sara_pets.walk()



# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

class Dog():
    def __init__(self, name, age, weight):
        self.name= name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        running_speed = self.weight / self.age * 10
        return f"{self.name} running speed is {running_speed}"
    
    def fight(self, other_dog, another_dog):
        self_score = self.run_speed() *self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        third_score = another_dog.run_speed()* another_dog.weight
        if self_score > other_score > third_score:
            return f"{self.name} is the winner "
        elif other_score > self_score > third_score:
            return f"{other_dog.name}is the winner"
        elif third_score > self_score > other_score:
            return f"{another_dog.name}is the winner"
        else:
            return "It's a draw"

dog1 = Dog("rex",3,15)
dog2 = Dog("firulais",5,25)
dog3 = Dog("cookie",4,8)

print(dog1.bark())
print(f"{dog1.name}'s running speed: {dog1.run_speed()}")

print(dog2.bark())
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")

print(dog3.bark())
print(f"{dog3.name}'s running speed: {dog3.run_speed()}")
print(dog1.fight(dog2, dog3))



# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.
