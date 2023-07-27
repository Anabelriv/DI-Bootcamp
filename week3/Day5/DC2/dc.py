# # Quizz
#       Class: It's a blueprint used in OOP to create objects, add attributes and methods that the objects will have, this helps to create objects with specific properties

#       Instance: This is the same as an object, each one has its own attributes and it can call the methods defined in the class

#       Encapsulation: It's the containeraziation of all the attributes and methods that function on the objects, within one class. It helps to also build methods privately and to allow some changes with getters and setters.

#       Abstraction: It's to simplify the complex codes building a program and to show only the essential feautures. 

#       Inheritance: it's a mechanism that allows a class to inherit properties from another class (super class), this can be done withuot redifining them 

#       Multiple inheritance: this mechanism allows a class to inherit from more than one base class.This is not programmer friendly and can raise complexities

#       Polymorphism: this allows objects from different classes to be like objects from a common class 

#       Method Resolution Order (MRO) is the order in which classes are searched for method resolution in a class hierarchy. 

# 

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
