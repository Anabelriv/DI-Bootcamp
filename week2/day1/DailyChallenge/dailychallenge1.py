import random
#Exercise 1

string= input("give me a string of 10 characters: ")
if len(string) == 10:
    print("perfect string")
elif len(string) <10:
    print("string too short")
else:
    print("string too long")

#Exercise 2

print(string[0],string[-1])

#Exercise 3
new_string=""
for char in string:
    new_string+= char
    print(new_string)

#Exercise 4
str_var= list(string)
random.shuffle(str_var)
new_random_string=''.join(str_var)
print(new_random_string)




