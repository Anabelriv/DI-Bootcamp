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


# implement the gt dunder method that receives 2 different employees, and returns the employee with the highest salary
# implement the add dunder method that that receives 2 different employees, and returns the total salary of the 2 employees
# implement the str dunder method that introduce the employee

# # Exercise Encapsulation
# make the address attribute private
# implement a method that return the address of the employee --> getter
# implement a method that modifies the address of the employee, only if the employee is older than 30--> setter
# implement a method create_best_employee that should create a new employee only if their salary is > 30000 --> class method

# Exercise 2
# Create a Manager class, that inherits from the Employee class With the attributes : firstname, lastname, adress, age, job is manager as default, salary is 45000 by default, list of employees empty by default
# Create 1 manager object and display his attribute
# Brad Pitt 50 years old
# Add those methods to the class
# add_new_employee(self, new_employee) : adds the new employee object to the list of employees
# show_employees(self) : show the fullnames of all the employees under the manager

class Employee():
    all_employees = []
    def __init__(self, firstname, lastname, age, job, salary):
        self.first_name = firstname
        self.last_name = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def __str__(self) :
        return f"the employee {self.first_name}{self.last_name} is {self.age} years old and his job is {self.job} and his salary is {self.salary}"
    
    def __repr__(self):
        return f"{self.first_name} - {self.last_name} - {self.age} - {self.job} - {self.salary}"
    
    def __gt__(self, other_employee):
        if self.salary > other_employee.salary:
            return self
        else :
            return other_employee
    
    def __add__(self, other_employee):
        return self.salary + other_employee.salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def happy_birthday(self):
        return self.age + 1
    
    def get_promotion(self,promotion_amount):
        promotion_amount = 200
        return self.salary + (promotion_amount)
    
    def show_info(self):
        print(f"The name is {self.get_full_name()}, the age is {self.age}, the job is {self.job}, the salary is {self.salary}")

    @classmethod
    def create_best_employee(cls, other_employee):
        if Employee.salary > other_employee.salary:
            return cls.all_employees.append(other_employee)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        if self.age > 30:
            self.__address = new_address

class Manager(Employee):
    def __init__(self, firstname, lastname, age, address, job = "Manager", salary = 45000):
        super().__init__(firstname, lastname, age, job, salary)
        self.address = address
        self.employees = []

    def add_new_employee(self, new_employee):
        self.employees.append(new_employee)

    def show_employees(self):
        print("Employees under the manager:")
        for employee in self.employees:
            print(employee.get_full_name())


# Creating a manager object
manager1 = Manager("Brad", "Pitt", 50, "Los Angeles, CA")
print(manager1)

# Creating employees
employee1 = Employee("Lea", "Smith", 30, "developer", 45000)
employee2 = Employee("David", "Schartz", 20, "teacher", 5000)

# Adding employees to the manager's list
manager1.add_new_employee(employee1)
manager1.add_new_employee(employee2)

# Showing the employees under the manager
manager1.show_employees()


user1 = Employee("Lea", "Smith",30,"developer", 45000)
other_employee = Employee("David", "Schartz",20,"teacher", 5000)

user1.address = "123 Main St"  # Setter will set address only if age is greater than 30
print(user1.address)  # Getter to access the address
# user1.show_info()
# user2.show_info()

# print(user1)
# print(user1 > user2)
# print(user1 + user2)
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
















