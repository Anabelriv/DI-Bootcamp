# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
import random

def display_message():
    print("I am learning Full Stack Python")

display_message()
print(display_message)

# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.
def favorite_book(title):
    sentence = "One of my favorite books is "
    print (sentence+ title)

favorite_book("all the light we cannot see")

# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.
def describe_city(city,country="Israel"):
    print(f'The city {city} is in the country {country}')

describe_city("Tel Aviv")


# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

def number(num):
    random_num=random.randint(0,100)
    if 1<= num >=100:
        print(random_num)
    if num == random_num:
        print("Success it's the same number")
    else:
        print(f"Fail this your number {num} and this was our number {random_num}")
    return random_num

number(3)
print(number)
    



# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size, message):
    print(f"The size is {size} and the text is {message}")

make_shirt("small", "You can do it")

def make_shirt2(size='Large', message="I love Python"):
    print(f"The size is {size} and the text is {message}")

make_shirt2()
make_shirt2("large")
make_shirt2("medium")
make_shirt2("xsmall","I love it too")
make_shirt2("xlarge", message="I love it more")



# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Create a function called show_magicians(), which prints the name of each magician in the list.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    for name in magician_names:
        print(name)
    return magician_names

show_magicians()
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
def make_great():
    for name in magician_names:
        print(name+" the Great")

make_great()

# Call the function show_magicians() to see that the list has actually been modified.
show_magicians() #it's not modified


# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
def get_random_temp():
    random_temp=random.randint(-10,40)
    return random_temp

get_random_temp()

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
def main():
    temperature=get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius")

    if temperature <0:
        print(f"{temperature} degrees is freezing cold, get your coat!")
    elif 16 <= temperature <= 23:
        print(f"{temperature} degrees is nice to take a jacket")
    elif 24 <= temperature <= 32:
        print(f"{temperature} degrees is getting hot, better stay inside with the AC on")
    else:
        print(f"{temperature} degrees is too hot, pack and move to the South Pole")

main()

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
def get_random_temp2():
    random_temp=random.randint(-10,40)
    if random_temp <16:
        season="winter"
    elif 17>= random_temp <=23:
        season="spring"
    elif 24>= random_temp <=32:
        season="autumn"
    else:
        season="summer"
    return season

get_random_temp2()


# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

def main2():
    user_season=input("Give me a season: ")
    temperature = get_random_temp(user_season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature <= 23:
        print("It's nice weather. You can take a jacket with you.")
    elif 24 <= temperature <= 32:
        print("It's getting hot, better stay inside with the AC on.")
    else:
        print("It's too hot, pack and move to the South Pole.")

main()


# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

def get_random_temp_month(month):
    if 1 <= month <= 2 or month == 12:
        season = "winter"
    elif 3 <= month <= 5:
        season = "spring"
    elif 6 <= month <= 8:
        season = "summer"
    elif 9 <= month <= 11:
        season = "autumn"
    else:
        raise ValueError("Invalid month. Enter a number between 1 and 12.")
    
    if season == "winter":
        random_temp = random.uniform(-10, 16)
    elif season == "spring":
        random_temp = random.uniform(17, 23)
    elif season == "autumn":
        random_temp = random.uniform(24, 31)
    else:  
        random_temp = random.uniform(32, 40)

    return random_temp

def main3():
    user_month = int(input("Give me the number of the month (1 = January, 12 = December): "))
    temperature = get_random_temp_month(user_month)
    print(f"The temperature right now is {temperature:.1f} degrees Celsius.")


main3()


# 🌟 Exercise 5 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.
def take_quiz():
    correct_answers=0
    incorrect_answers=0
    wrong_answers=[]

    for question_data in data:
        question=question_data['question']
        correct_answer=question_data['answer']

        user_answer = input(question + " ")
        user_answer = user_answer.strip().capitalize()

        if user_answer == correct_answer:
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer
            })

    print("\nQuiz completed!")
    print(f"Number of correct answers: {correct_answers}")
    print(f"Number of incorrect answers: {incorrect_answers}")

    if incorrect_answers > 0:
        print("\nWrong answers:")
        for i, wrong_answer in enumerate(wrong_answers, 1):
            print(f"{i}.")
            print(f"   Question: {wrong_answer['question']}")
            print(f"   Your answer: {wrong_answer['user_answer']}")
            print(f"   Correct answer: {wrong_answer['correct_answer']}")

    if incorrect_answers > 3:
        print("\nYou had more than 3 wrong answers.Try again")

take_quiz()
