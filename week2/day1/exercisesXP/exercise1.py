# Exercise 1
print("Hello World\n" *3)

# Exercise 2
print((99^3)*8)

# Exercise 3
# False
# True
# error, can't compare int to str
# error, can't compare str to int
# False (case sensitive)


# Exercise 4
computer_brand= "Mac"
print(f"I have a {computer_brand} computer")

#Exercise 5
name= "Anabel"
age= "32"
shoe_size="8"
info=f"I am {name} and I have {age} years old and my shoes are size {shoe_size}"
print(info)

#Exercise 6: A&B
a= 4
b= 7
if a> b:
    print("Hello World")
else:
    print("end")

#Exercise 7
user_input= int(input("Enter a number "))
if user_input % 2 == 0:
    print("Your number is even")
else:
    print("your number is odd")


#Exercise 8
user_name= input("What is your name? ").capitalize()
my_name= "Anabel"
if user_name == my_name:
    print("How cool we have the same name!!")
else:
    print("your name is a bit boring")

#Exercise 9
height=float(input("What is your height in inches? "))
minimum_height= 145
inches_to_cm= height* 2.54
if inches_to_cm >= minimum_height:
    print("You can go on the ride")
else:
    print("sorry, you are too short")
