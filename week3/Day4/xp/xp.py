import random

#Generate random sentence:
def generate_random_sentence(length, words_list):
    if length < 1:
        raise ValueError("Sentence length must be greater than 0.")
    if not words_list or len(words_list) < 1:
        raise ValueError("The words list is empty or invalid.")

    sentence = " ".join(random.choice(words_list) for _ in range(length))
    return sentence.capitalize() + "."

def main():
    words_list = ["hello", "world", "python", "is", "fun", "exercise", "generator", "random"]

    print("Welcome to the Random Sentence Generator!")
    
    try:
        length = int(input("Enter the desired sentence length: "))
        sentence = generate_random_sentence(length, words_list)
        print("Generated sentence:", sentence)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

# This function should read the file’s content and return the words as a collection.
def get_words_from_file():
    try:
        with open("words.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("Error: The 'words.txt' file was not found.")
        return []

# takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have.
def get_random_sentence(length, words):
    if length < 2 or length > 20:
        raise ValueError("Error: Sentence length should be between 2 and 20.")
    return " ".join(random.choices(words, k=length)).lower()

def main():
    print("Welcome to the Random Sentence Generator!")
    
    words = get_words_from_file()
    if not words:
        return  # Stop the program if the word list is empty or not found
    
    while True:
        try:
            length = int(input("Enter the desired sentence length (2-20): "))
            sentence = get_random_sentence(length, words)
            print(f"Generated sentence: {sentence}")
            break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()


# 🌟 Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.