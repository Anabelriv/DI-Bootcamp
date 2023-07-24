# sentence = 'hello'

# isinstance('hello',str)

# class Dog:
#     def __init__(self,name,age):
#         self.dog_name = name
#         self.dog_age = age

#     def bark(self):
#         print(f"The {self.dog_name} barks")
        
#     def jump(self):
#         print(f"{self.dog_name} jumps")
# #inheritance
# class GermanShepard(Dog):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.big_ears = True

#     def run(self):
#         super().bark()
#         print("the dog can run")


# german_sherman_one = GermanShepard("tom",2)
# german_sherman_one.run()

# my_dog = Dog("Rex")

# my_dog.bark()
# print(my_dog.dog_name)

# my_friend_dog = Dog("Lola")
# print(my_friend_dog.dog_name)

# print(my_dog) #--> prints the object at the memory place 
# dir(my_dog) #---> shows me the methods I have in this class

# Exercise 1 : Basic Classes
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary
# Create 2 users object and display their attribute Lea Smith 30 years old developer David Schartz 20 years old teacher
# Add those methods to the class
# get_fullname(self) : that return the firstname + lastname
# happy_birthday(self) : that return the age incremented by one
# get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# show_info(self) : that will print the information of the employee --> name, age, job, salary
# Call all the methods

class Employee():
    def __init__(self, firstname, lastname, age, job, salary):
        self.first_name = firstname
        self.last_name = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def happy_birthday(self):
        return self.age + 1
    
    def get_promotion(self,promotion_amount):
        promotion_amount = 200
        return self.salary + (promotion_amount)
    
    def show_info(self):
        print(f"The name is {self.get_full_name()}, the age is {self.age}, the job is {self.job}, the salary is {self.salary}")

user1 = Employee("Lea", "Smith",30,"developer", 45000)
user2 = Employee("David", "Schartz",20,"teacher", 5000)

user1.show_info()
user2.show_info()

# Exercise 2 : Inheritance
# Create a Developer class, that inherits from the Employee class with the attributes :
# firstname, lastname, age,
# job is developer as default,
# salary is 15000 by default,
# coding skills (a list by default) : all developers should start with an empty list of skills
# Create 2 developer objects and display their attribute
# Tom Cruiz 30 years old
# Angelina Jolie 23 years old
# Add those methods to the class
# add_skills(self, *skills) : receives a tuple of skills and append them to the coding skills list
# coding(self) : print a nice sentence with all the coding languages the developer knows
# coding_with_partner(self, other_developer) : print a nice sentence with the name of both developers, and their skills
# override the get_promotion(self, promotion_amount) : that multiplies the salary of the user by the promotion
# Call all the methods, also those from the Employee Class


class Developer (Employee):
    def __init__(self, firstname, lastname, age, job = 'Developer', salary = 15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.coding_skills = []

    
    def add_skills(self,*coding_skills):
        self.coding_skills.extend(coding_skills)

    def coding(self):
        skills = ', '.join(self.coding_skills)
        print(f"the developer {self.get_full_name()} knows all these coding languages: {skills}")

    def coding_with_partner(self, other_developer):
        self.coding()
        other_developer.coding()

        print(f"the developers {self.name} and {self.name} are working together")
        print(f"{self.get_full_name()} knows: {self.skills}")
        print(f"{other_developer.get_full_name()} knows: {', '.join(other_developer.coding_skills)}")

    def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount 
        return self.salary

dev1 = Developer("Tom", "Cruiz", 30)
dev2 = Developer("Angelina", "Jolie", 23)


dev1.add_skills("Python", "JavaScript", "C++")
dev2.add_skills("Java", "HTML", "CSS")

# Display attributes
dev1.show_info()
dev1.coding()

dev2.show_info()
dev2.coding()

# Coding together
dev1.coding_with_partner(dev2)

# Promotion
promotion_amount = 5000
new_salary1 = dev1.get_promotion(promotion_amount)
new_salary2 = dev2.get_promotion(promotion_amount)
print(f"{dev1.get_full_name()}'s new salary: {new_salary1}")
print(f"{dev2.get_full_name()}'s new salary: {new_salary2}")
















