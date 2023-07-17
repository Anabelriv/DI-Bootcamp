#challenge1
number_user=int(input("enter a number: "))
length_user=int(input("enter a length: "))

multiples=[]
count= 1
while len(multiples)< length_user:
    multiple=number_user*count
    multiples.append(multiple)
    count+=1

print("List of multiples:", multiples)

#challenge2
user_word=input("enter a word: ")
new_word=""

char_before=""
for char in user_word:
    if char != char_before:
        new_word += char
        char_before = char

print("New word:", new_word)