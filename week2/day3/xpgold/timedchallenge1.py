
#write down your logic here 

# Get the input sentence from the user
input_str = input("Enter a sentence: ")

# Split the sentence into words using whitespace as the separator
words = input_str.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed words back into a sentence
reversed_sentence = " ".join(reversed_words)

# Print the reversed sentence
print(reversed_sentence)
