# Exam
# Python Basics

# Data Types

# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple --> answer
# d) Set


# Lists and Loops

# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.
list_of_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(list_of_squares)

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.
numbers = list(range(1, 11))

divisible_by_2_and_3 = [x for x in numbers if x % 2 == 0 and x % 3 == 0]

print(divisible_by_2_and_3)


# Loop through the provided list of dictionaries and print the names and ages:

student_list = [
    {"name": "John", "age": 24},
    {"name": "Anna", "age": 22},
    {"name": "Mike", "age": 25},
]

for student in student_list:
    name = student["name"]
    age = student["age"]
    print(f"Name: {name}, Age: {age}")
# Function Behavior with *args and **kwargs

# Write a function combine_words that accepts any number of positional arguments and key-value arguments. The function should return a single sentence combining all the words provided.
# Example:
# print(combine_words("Hello", "world", second="is", third="great!", first="Python"))
# Expected Output:
# "Hello world. Python is great!"


def combine_words(*args, **kwargs):
    words = " ".join(args)
    if kwargs:
        words += " " + " ".join(kwargs.values())
    sentence = words.capitalize() + "."
    return sentence


# Testing
print(combine_words("Hello", "world.", second="is", third="great!", first="Python"))


# Object-Oriented Programming (OOP)


# Create a class Vehicle with string attributes type, brand, and integer attribute year. Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.
class Vehicle:
    def __init__(self, type_, brand, year):
        self.type = type_
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Type: {self.type}, Brand: {self.brand}, Year: {self.year}"


# Testing

car = Vehicle("Car", "Jeep", 2022)
print(car)


# OOP Inheritance and Decorators

# Create a class Car with string attributes brand, model, and integer attribute mileage. Implement a method to return the car’s details.


class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def car_details(self):
        return (
            f"Brand: {self.brand}, Model: {self.model}, Mileage: {self.mileage} miles"
        )


# testing
car = Car("Toyota", "Camry", 50000)
print(car.car_details())


# Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. Override the car’s details method to include the battery capacity.
class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery_capacity):
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    # Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.
    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = new_capacity
        else:
            print("Battery capacity must be a positive value.")

    def car_details(self):
        return (
            f"{super().car_details()}, Battery Capacity: {self.__battery_capacity} kWh"
        )


# Testing
electric_car = ElectricCar("Tesla", "Model S", 20000, 100)
print(electric_car.car_details())

# Testing property
print(electric_car.battery_capacity)

# Testing battery_capacity setter
electric_car.battery_capacity = 120

# testing a negative battery capacity
electric_car.battery_capacity = -50

# Displaying car details
print(electric_car.car_details())


# Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created and a static method for a bank policy message. Ensure the balance is non-negative.


class BankAccount:
    num_accounts = 0

    # bank policy message
    @staticmethod
    def bank_policy_message():
        return "Thank you for trusting us!"

    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder
        self._balance = max(initial_balance, 0)
        BankAccount.num_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 <= amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def view_balance(self):
        return self._balance

    @classmethod
    def total_accounts(cls):
        return cls.num_accounts


# Testing
account1 = BankAccount("Bob", 1000)
account2 = BankAccount("Billy", 500)

print(account1.view_balance())
account1.deposit(300)
account1.withdraw(200)
print(account1.view_balance())

print(account2.view_balance())
account2.withdraw(100)
print(account2.view_balance())

print("Total accounts:", BankAccount.total_accounts())
print(BankAccount.bank_policy_message())


# Data Science

# Numpy and Pandas Visualization

# Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().
# import numpy as np

# array = np.arange(1, 10).reshape(3, 3)
# print(array)

# Provided pandas DataFrame df:

# import pandas as pd

# df = pd.DataFrame({"A": [1, "apple", 3, 4, "banana"], "B": [5, 6, 7, 8, 9]})


# Replace non-numeric values in column “A” with the mean of numeric values. Plot a histogram of the “A” column using matplotlib.
# import matplotlib.pyplot as plt

# df["A"] = pd.to_numeric(df["A"], errors="coerce")
# mean_value = df["A"].mean()
# # Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.
# plt.hist(df["A"], bins=10)
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram of A")
# plt.show()
# Django and Django REST

# Create a new Django project called ‘academy’. After that - create a new app (inside the ‘academy’ project) called ‘school’.
# Done

# Django Models with Foreign Key

# Define Django models Teacher and Course. Course has course_name (CharField) and course_code (CharField). Teacher has name (CharField). Create a many-to-many relationship between Teacher and Course.
# Done

# Views

# Create a Django view course_details to fetch details of a course by its id.


# Use a APIview for Teacher to display all teachers.


# Full App

# Create a base model SchoolFacility with facility_name (CharField) and usage_purpose (TextField).


# Create a Laboratory model inheriting from SchoolFacility with equipment_list (TextField).


# Create views for all school facilities and another for only laboratories.


# Create a serializer for SchoolFacility and another for Laboratory to convert to JSON. Test using Postman.
