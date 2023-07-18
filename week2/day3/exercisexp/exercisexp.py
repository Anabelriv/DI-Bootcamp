# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result=  dict(zip(keys,values))
print(result)

# Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
ticket_prices ={3:10,12:15}
price_per_person={}
total_cost=0

for name,age in family.items():
    if age <3:
        cost="0"
    elif age >3 and age <12:
        cost = ticket_prices[3]
    else:
        cost = ticket_prices[12]

    price_per_person[name] = total_cost
    total_cost += cost

for name, cost in price_per_person.items():
    print(f"{name} total cost is $ {cost}")

print(f"Total bill for the family is : $ {total_cost}")

# Bonus
family = {}
ticket_prices = {3: 10, 12: 15}

num_family_members = int(input("Enter the number of family members: "))

for i in range(num_family_members):
    name = input("Enter the name of family member: ")
    age = int(input("Enter the age of family member: "))
    family[name] = age

price_per_person = {}
total_cost = 0

for name,age in family.items():
    if age <3:
        cost="0"
    elif age >3 and age <12:
        cost = ticket_prices[3]
    else:
        cost = ticket_prices[12]

    price_per_person[name] = total_cost
    total_cost += cost

for name, cost in price_per_person.items():
    print(f"{name} total cost is $ {cost}")

print(f"Total bill for the family is : $ {total_cost}")

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand={
    'name':'Sara',
    'creation_date': '1975', 
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton'], 
    'number_stores': '7000', 
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']}
}
# 3. Change the number of stores to 2.
brand['number_stores']='2'
# 4. Print a sentence that explains who Zaras clients are.
client_types = brand['type_of_clothes']
print(f"Zara's clients are: {client_types} related items")
# 5. Add a key called country_creation with a value of Spain.
brand['country_creation']='Spain'
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'international_competitors' in brand:
    print("Yes it is")
else:
    print('No')
# 7. Delete the information about the date of creation.
del brand['creation_date']
# 8. Print the last international competitor.
print(brand['international_competitors'][-1])
# 9. Print the major clothes colors in the US.
print(brand['major_color']['US'])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))
# 11. Print the keys of the dictionary.
print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000
more_on_zara={
    'creation_date':'1975',
    'number_stores':'10000'
}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)

# 14. Print the value of the key number_stores. What just happened ?
print(brand['number_stores']) #--- The number was changed

# Exercise 4 : Disney Characters
# Instructions
# Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# #1/
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

disney_users_A= {user:index for index, user in enumerate(users)}
print(disney_users_A)

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

# #2/
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B={}
for index, user in enumerate(users):
    disney_users_B[index]=user
print(disney_users_B)
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# #3/ 
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
disney_users_C= {user:index for index, user in enumerate(sorted(users))}
print(disney_users_C)
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

# The characters, which names start with the letter “m” or “p”.
disney_users_modified_1 = {user: index for index, user in enumerate(users) if 'i' in user or user[0] in ['m', 'p']}
print(disney_users_modified_1)
