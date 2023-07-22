
# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:
# 18,22,24
import math
from statistics import mean

def calculate_value(D_values):
    C = 50
    H = 30
    results = []

    for D in D_values:
        Q = math.sqrt((2 * C * D) / H)
        results.append(round(Q))

    return results

user_input = input("Enter comma-separated numbers: ")
D_values = [int(num) for num in user_input.split(",")]

output_values = calculate_value(D_values)
output_string = ",".join(str(val) for val in output_values)
print(output_string)


# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:

a = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
b = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
c = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
d = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.
num_list=(a+b+c+d)
# Print the following information:

# a. The list of numbers – printed in a single line
print(num_list)
# b. The list of numbers – sorted in descending order (largest to smallest)
print(sorted(num_list, reverse=True))
# c. The sum of all the numbers
print(sum(num_list))
# A list containing the first and the last numbers.
first_and_last = [num_list[0], num_list[-1]]
print(first_and_last)
# A list of all the numbers greater than 50.
greater_50 = [num for num in num_list if num > 50]
print(greater_50)
# A list of all the numbers smaller than 10.
lower_10 = [num for num in num_list if num <10]
print(lower_10)
# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
squared_num = [num ** 2 for num in num_list]
print(squared_num)
# The numbers without any duplicates – also print how many numbers are in the new list.
unique_numbers=(list(set(num_list)))
print(unique_numbers)
print(len(unique_numbers))
# The average of all the numbers.
print(mean(num_list))
# The largest number.
largest_number = max(num_list)
print(largest_number)
# 10.The smallest number.
smallest_number = min(num_list)
print(smallest_number)
# 11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
# 12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
# 13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# 14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# 15.Bonus: Will the code work when the number of random numbers is not equal to 10?

# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

paragraph = """
Machine learning is a subset of artificial intelligence (AI) that focuses on teaching computers how to learn and improve from experience without being explicitly programmed. It is a rapidly growing field that has applications in various industries, such as healthcare, finance, marketing, and more.

One of the key concepts in machine learning is the use of algorithms to process and analyze data. These algorithms enable computers to identify patterns, make predictions, and optimize decision-making based on the data they receive.

Machine learning can be categorized into two main types: supervised learning and unsupervised learning. In supervised learning, the algorithm is trained using labeled data, where the correct outputs are provided. On the other hand, unsupervised learning involves training the algorithm on unlabeled data and letting it find patterns on its own.

Another important aspect of machine learning is the need for large datasets. The performance of machine learning models improves with more data, allowing them to make more accurate predictions and decisions.

Overall, machine learning has the potential to revolutionize various industries and make processes more efficient and intelligent.
"""

# How many characters it contains
num_characters = len(paragraph)

# How many sentences it contains
num_sentences = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")

# How many words it contains
word_list = paragraph.split()
num_words = len(word_list)

# How many unique words it contains
unique_words = set(word_list)
num_unique_words = len(unique_words)

# How many non-whitespace characters it contains
non_whitespace_characters = len(paragraph.replace(" ", ""))

# The average amount of words per sentence in the paragraph
average_words_per_sentence = num_words / num_sentences

# The amount of non-unique words in the paragraph
num_non_unique_words = num_words - num_unique_words

# Print the analysis
print("Number of characters:", num_characters)
print("Number of sentences:", num_sentences)
print("Number of words:", num_words)
print("Number of unique words:", num_unique_words)
print("Number of non-whitespace characters:", non_whitespace_characters)
print("Average words per sentence:", average_words_per_sentence)
print("Number of non-unique words:", num_non_unique_words)

# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1
input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# Remove punctuation marks and split the input text into words
words = input_text.replace(".", "").replace("?", "").split()

# Create an empty dictionary to store the word frequencies
word_freq = {}

# Count the frequency of each word
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Print the word frequencies
for word, frequency in word_freq.items():
    print(f"{word}:{frequency}")


