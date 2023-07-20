# Challenge 1 : Sorting
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

word_sequence= input("Write a list of words separated by a comma")
words_list= [word.strip()for word in word_sequence.split(",")]
sorted_words = sorted(words_list)
output_sequence=",".join(sorted_words)
print(output_sequence)

# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples

# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

# longest_word("A thing of beauty is a joy forever.") ➞ "forever."

# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"


def longest_word(sentence):
    #split the words
    word_list=[word.strip() for word in sentence.split(" ")]

    longest_word =""
    max_length=0
    # loop through each word
    for word in word_list:
        word_length =len(word)
        #compare the lengths
        if word_length > max_length:
            longest_word= word
            max_length = word_length
    return longest_word

# # Test cases
print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!"))  
print(longest_word("Hi I'm learning Python in Developers Institute"))
