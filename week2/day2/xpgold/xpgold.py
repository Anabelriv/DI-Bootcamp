from random import randint
# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.
a= [1,2,3]
b= [4,5,6]
a.extend(b)
print(a)


# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
multiple_7 =[]
multiple_5 = []
for x in range(1500,2500):
    if x %7 == 0:
        multiple_7.append(x)
    elif x %5 ==0:
        multiple_5.append(x)

#print(f"this list is multiple of 5 {multiple_5} \nand this list is multiple of 7  {multiple_7}")

# Exercise 3: Check The Index
# Instructions
# Using this variable
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
print(names.index(input("Choose a name from these to give you the index: 'Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus': ")))



# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87
num1=input("Give me a digit: ")
num2=input("Give me a second digit: ")
num3=input("Give me a third digit: ")

if num3< num1 > num2:
    print("num1 is the greatest number")
elif num3 <num2 > num1:
     print("num2 is the greatest number")
else:
    print("num3 is the greatest number")

print(num1, num2, num3)


# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y','z']
vowel=['a','e','i','o','u']
message_1=["It's a vowel"]
message_2=["It's a consonant"]

for letter in alphabet:
    if letter in vowel:
        print(f"{letter} -- {message_1}")
    else:
        print(f'{letter} -- {message_2}')
print(letter)




# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

letter = input("Enter a single character: ")

for word in words:
    if letter in word:
        index = word.index(letter)
        print(f"The first appearance of '{letter}' in '{word}' is at index {index}.")
    else:
        print(f"'{letter}' does not exist in '{word}'.")


# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

num_list=range(1,1000001)
print(min(num_list), max(num_list))
print(sum(num_list))

# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

comma_numbers=input("Write a sequence of numbers separated by comma")
sequence=comma_numbers.split(",")
number_tuple= tuple(sequence)
print(sequence)
print(number_tuple)


# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.
games_won=0
games_lost=0

while True:
    user_number = input("Give a number from 1 to 9 including or type 'q' to exit: ")
    if user_number.lower() == 'q':
        print("Thanks for playing")
        break
    
    random_number = randint(1, 9)

    if int(user_number) == random_number:
        print("You are the winner")
        games_won += 1
    else:
        print(f"Better luck next time, this was the random number: {random_number}")
        games_lost += 1

print(f"This is how many games you won {games_won},and this is how many you lost {games_lost}")