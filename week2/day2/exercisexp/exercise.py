# Exercise 1
my_fav_numbers_set = {3,5,7,13}
my_fav_numbers_set.update([1,32])
my_fav_numbers_set.discard(13)
my_fav_numbers_set= list(my_fav_numbers_set)
my_fav_numbers_set.pop()
print(my_fav_numbers_set)

friend_fav_numbers= {2345,2039584,2093,8739487,983724}
our_fav_numbers= my_fav_numbers_set.union(friend_fav_numbers)
print(our_fav_numbers)
print("Exercise 1")
# Exercise 2
#We can create a new tupple but the same tupple can't be edited

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop(0)
basket.pop()
basket.append("Kiwi")
basket.insert(0,"Apples")
count_apples= basket.count("Apples")
basket.clear()
print(basket)
print("Exercise 3")
# Exercise 4
#Float are for decimal numbers
start_value = 0.0
end_value = 1.0
increment = 0.1

current_value = start_value
while current_value <= end_value:
    print(current_value)
    current_value += increment

first_value=1.0
last_value=5.0
increment=0.5
current_value=first_value
while current_value <= last_value:
    print(current_value)
    current_value += increment

print("Exercise 4")

# Exercise 5
for x in range(0,21):
    print(x)

for i in range(1, 21, 2):
    print(i)
    
print("Exercise 5")

# Exercise 6
my_name="Anabel"
user_name=input("Give me your name: ").capitalize()

while my_name != user_name:
    user_name=input("Give me your name: ").capitalize()

print("thanks we have the same name!")

print("Exercise 6")

# Exercise 7
user_fav_fruit=input("Tell me your favorite fruits separated by space: ")
list_user_fruits = list(user_fav_fruit.split(" "))

while True:
    fruit_name = input("Please tell me the name of a fruit (or 'quit' to exit): ")
    
    if fruit_name.lower() == "quit":
        break
    
    if fruit_name in list_user_fruits:
        print("You chose one of your favorite fruits! Enjoy!")
    else:
        print("You chose a new fruit. I hope you enjoy!")

print("Exercise7")
# Exercise 8
cost_topping= 2.5
pizza_pie=10
total_toppings=[]

while True:
    pizza_topping = input("Please tell me a pizza topping to add (or 'quit' to exit): ")
    
    if pizza_topping.lower() == "quit":
        break
    
    else:
        print("I will add that topping to the pizza")
        total_toppings.append(pizza_topping)

count_topping = len(total_toppings)
toppings_total_cost=(cost_topping*count_topping)
total_cost= (pizza_pie + toppings_total_cost)
print(f"Your total is {total_cost}")

print("Exercise 8")

# Exercise 9
num_people = int(input("Enter the number of people in the family: "))
ages = []

for i in range(num_people):
    age = int(input("Enter the age of person {}: ".format(i+1)))
    ages.append(age)

# Calculate the total cost of tickets for the family
total_cost = 0

for age in ages:
    if age < 3:
        total_cost += 0
    elif age >= 3 and age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print("The total cost of tickets for the family is: $", total_cost)

# Remove teenagers who are not permitted to watch the movie
final_list = []

for age in ages:
    if age >= 16 and age <= 21:
        final_list.append(age)

print("The final list of teenagers permitted to watch the movie:")
print(final_list)

#Exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    
for sandwich in finished_sandwiches:
    print("I made your", sandwich.lower())

