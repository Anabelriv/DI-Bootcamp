# Exercise 1 complete
# Exercise 2 
# Exercise 3
## True
## True
## False
## False
## True
## False
##  True, False, 5, 10
#Exercise 4

my_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
print(len(my_text))

#Exercise 5
long_sentence=input("Give me the longest sentence without the letter a: ")
a="a"
if a in long_sentence:
    print("you got an a in the sentence sorry, try again")

else:
    print("great give me another sentence")

second_long_sentence=input("type:")
if a in second_long_sentence:
    print("you got an a in the sentence sorry, try again")

elif len(long_sentence)> len(second_long_sentence):
    print("Congrats you got a longer sentence")

else:
    print("It wasn't longer sorry")





