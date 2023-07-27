# # Quizz
# # Class: It's a blueprint used in OOP to create objects, add attributes and method that the objects will have, this helps to create objects with specific properties
# # Instance: This is the same as an object, each one has its own attributes and it can call the methods defined in the class
## Encapsulation: It's the containeraziation

# 3. What is encapsulation?
#    Encapsulation is one of the four fundamental principles of object-oriented programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on that data, within a single unit (class). The main idea is to hide the internal implementation details of the class from the outside world, allowing access to the data through well-defined methods (getters and setters). This concept helps achieve data abstraction and information hiding.

# 4. What is abstraction?
#    Abstraction is another fundamental principle of OOP. It is the process of simplifying complex systems by representing only the essential features and ignoring irrelevant details. In Python, abstraction can be achieved through abstract classes and interfaces. It allows developers to create a blueprint or a model for a class without implementing all the methods, thus providing a clear separation between the interface and implementation.

# 5. What is inheritance?
#    Inheritance is a mechanism in object-oriented programming that allows a class (called the derived or subclass) to inherit properties and behaviors from another class (called the base or superclass). The derived class can access the attributes and methods of the base class without redefining them. It promotes code reuse and helps in creating a hierarchical relationship among classes.

# 6. What is multiple inheritance?
#    Multiple inheritance is a feature in some object-oriented programming languages, including Python, that allows a class to inherit from more than one base class. This means a derived class can access attributes and methods from multiple parent classes. However, multiple inheritance can lead to complexities and the "diamond problem" if not handled carefully.

# 7. What is polymorphism?
#    Polymorphism is a concept in OOP that allows objects of different classes to be treated as objects of a common base class. It enables a single interface to represent different data types or classes. In Python, polymorphism is typically achieved through method overriding, where derived classes provide their own implementation for methods with the same name as the base class.

# 8. What is method resolution order or MRO?
#    Method Resolution Order (MRO) is the order in which classes are searched for method resolution in a class hierarchy. In Python, when a method is called on an object, the interpreter searches for the method in the class of the object, and if not found, it searches in the parent classes in a specific order determined by the C3 linearization algorithm. The MRO ensures that the correct method is invoked when there is multiple inheritance and avoids ambiguity in method resolution.
# #
# #
# #

# # Part 2: Create A Deck Of Cards Class.
# # The Deck of cards class should NOT inherit from a Card class.

# # The requirements are as follows:

# # The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# # The Deck class :
# # should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# # should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.


import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.is_empty():
            return self.cards.pop()
        else:
            print("The deck is empty. No more cards to deal.")
            return None

    def is_empty(self):
        return len(self.cards) == 0
