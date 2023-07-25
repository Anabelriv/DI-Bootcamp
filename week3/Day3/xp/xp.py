# from random import randint, choice
# import string
from faker import Faker
# from datetime import date, datetime
# # Exercise 1: Currencies
# # Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

# #     #Your code starts HERE
#     def __str__(self):
#         return f"{self.amount} {self.currency}"

#     def __int__(self):
#         return self.amount

#     def __repr__(self):
#         return f"{self.amount} {self.currency}"

#     def __add__(self, other):
#         if isinstance(other, Currency) and self.currency == other.currency:
#             return Currency(self.currency, self.amount + other.amount)
#         elif isinstance(other, (int, float)):
#             return Currency(self.currency, self.amount + other)
#         else:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

#     def __iadd__(self, other):
#         if isinstance(other, Currency) and self.currency == other.currency:
#             self.amount += other.amount
#         elif isinstance(other, (int, float)):
#             self.amount += other
#         else:
#             raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#         return self


# # Test cases
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))     # Output: '5 dollars'
# print(int(c1))     # Output: 5
# print(repr(c1))    # Output: '5 dollars'
# print(c1 + 5)      # Output: 10
# print(c1 + c2)     # Output: 15
# print(c1)          # Output: '5 dollars'

# c1 += 5
# print(c1)          # Output: '10 dollars'

# c1 += c2
# print(c1)          # Output: '20 dollars'

# # The next line will raise a TypeError
# print(c1 + c3)     
# # 🌟 Exercise 2: Import
# # Instructions
# # In a file named func.py create a function that adds 2 number, and prints the result
# # In a file namedexercise_one.py import and the function
# # Hint: You can use the the following syntaxes:

# # import module_name 

# # OR 

# # from module_name import function_name 

# # OR 

# # from module_name import function_name as fn 

# # OR

# # import module_name as mn


# # 🌟 Exercise 3: Random Module
# # Instructions
# # Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# # if it’s the same number, display a success message to the user, else don’t.

# def rolled_dice_check (number):
#     if not 1<= number <= 100:
#         raise ValueError("Number must be between 1 and 100.")
    
#     rolled_number = randint(1,100)
    
#     if number == rolled_number:
#         print(f"Success! You rolled a {rolled_number}.")
#     else:
#         print(f"You missed! the rolled number was {rolled_number}")


# user_input = int(input("Enter a number between 1 and 100: "))
# rolled_dice_check(user_input)

# # 🌟 Exercise 4: String Module
# # Instructions
# # Generate random String of length 5
# # Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# # Hint: use the string module

# letters = string.ascii_letters
# print ( ''.join(choice(letters) for i in range(5)))

# # 🌟 Exercise 5 : Current Date
# # Instructions
# # Create a function that displays the current date.
# # Hint : Use the datetime module.
# today = date.today()
# print("Today's date:", today)

# # Exercise 6 : Amount Of Time Left Until January 1st
# # Instructions
# # Create a function that displays the amount of time left from now until January 1st.
# # (Example: the 1st of January is in 10 days and 10:34:01hours).


# def time_left_until_january1st():
#     time_left = datetime.date(2024,1,1) - datetime.today
#     return f"new year will be {time_left}"


# # Test the function
# time_left_until_january1st()

# # Exercise 7 : Birthday And Minutes
# # Instructions
# # Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

# def minutes_lived(birthdate):
#     birthdate_format = "%Y-%m-%d"  # Choose the format of the birthdate, for example, "YYYY-MM-DD"
#     birthdate_obj = datetime.strptime(birthdate, birthdate_format)
#     now = datetime.now()

#     time_lived = now - birthdate_obj
#     minutes = time_lived.total_seconds() / 60

#     print(f"You have lived for approximately {minutes:.2f} minutes.")

# # Test the function
# birthdate = "1991-03-23"  # Replace this with the birthdate in the format "YYYY-MM-DD"
# minutes_lived(birthdate)


# Exercise 8 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.


def create_fake_user():
    fake = Faker()
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code(),
    }
    return user

def add_fake_users(users, num_users):
    for _ in range(num_users):
        user = create_fake_user()
        users.append(user)

# Create an empty list called users
users = []

# Add new dictionaries to the users list
num_users_to_add = 5
add_fake_users(users, num_users_to_add)

# Print the list of users
for user in users:
    print(user)