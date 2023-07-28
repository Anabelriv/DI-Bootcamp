# # Exercise 1
# birthdays = {
#     'Daysi': '16/05/1985',
#     'Anabel': '23/03/1990',
#     'Bob':'01/01/1990',
#     'Tom':'10/09/1999',
#     'Alex':'22/09/1980'
# }

# name = input("Give me a name and I will give you their birthdate (Daysi, Anabel, Tom, Bob, Alex): ")

# birthday = birthdays.get(name)

# if birthday:
#     print(f'The birthday of {name} is on this date {birthday}')
# else:
#     print(f"Sorry, there is no information for the name '{name}' in the list.")

# # Exercise 2 
# print(birthdays.keys())

# # Exercise 3
# new_name = input("Give me your name: ")
# new_birthdate = input ("What is your birthdate in this format DD/MM/YYYY: ")
# birthdays[new_name] = new_birthdate

# print(birthdays)

# Exercise 4 

# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# for k, v in dict.items(items):
#     print(k, v)

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0

for item, details in items.items():
    price = details['price']
    stock = details['stock']
    total_cost += price * stock

print(f"The total of the cost of stock is {total_cost}")
