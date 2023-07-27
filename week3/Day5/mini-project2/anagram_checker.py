# Instructions

# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

# Note: None of the methods in the class should print anything.
 
# anagram_checker.py

class AnagramChecker:
# Opening the file and adding them to a unique value list in lower case
    def __init__(self, word_list_file):
        word_list_file = '/Users/anabelrivera/Desktop/Bootcamp/DI-Bootcamp/week3/Day5/mini-project2/words_alpha.txt'
        with open(word_list_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file)

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        return [w for w in self.word_list if self.is_anagram(word, w)]
