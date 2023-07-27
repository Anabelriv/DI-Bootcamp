# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.


# anagrams.py

from anagram_checker import AnagramChecker

def get_user_input():
    word = input("Enter a word (or 'exit' to quit): ").strip().lower()
    return word

def validate_word(word):
    if len(word.split()) > 1:
        print("Error: Please enter only one word.")
        return False
# Return False if the characters are not alphabet letters
    if not word.isalpha():
        print("Error: Please enter alphabetic characters only.")
        return False
    return True

def main():
    word_list_file = '/Users/anabelrivera/Desktop/Bootcamp/DI-Bootcamp/week3/Day5/mini-project2/words_alpha.txt'
    anagram_checker = AnagramChecker(word_list_file)

    while True:
        word = get_user_input()

        if word == 'exit':
            break

        if not validate_word(word):
            continue

        if anagram_checker.is_valid_word(word):
            anagrams = anagram_checker.get_anagrams(word)
            print(f"YOUR WORD: {word.upper()}")
            print("This is a valid English word.")
            print(f"Anagrams for your word: {', '.join(anagrams)}.\n")
        else:
            print(f"YOUR WORD: {word.upper()}")
            print("This is NOT a valid English word.\n")

if __name__ == "__main__":
    main()
