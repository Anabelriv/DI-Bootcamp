# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]

class Family:
    def __init__(self, last_name):
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}]
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs ['name']} was born into the family.")
    
    def is_18(self,name):
        for member in self.members:
            if member['name'] == name:
                return member ['age'] >= 18
        return False
            
    def family_presentation(self):
        print(f"Family last name : {self.last_name}")
        print("Family members")
        for member in self.members:
            print(f" - {member['name']}")

family = Family("Thomson")

# Test the born method
family.born(name='Amelia', age=1, gender='Female', is_child=True)

# Test the is_18 method
print(f"Is Michael over 18? {family.is_18('Michael')}")
print(f"Is Amelia over 18? {family.is_18('Emma')}")

# Test the family_presentation method
family.family_presentation()





# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to 
# add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.

# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.
class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}]
    
    def use_power(self,name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:    
                    print(f"{name}'power is: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 yeasrs old")
     

    def incredible_presentation(self):
        super().family_presentation()
        print("Incredible members:")
        for member in self.members:
            print(f" - {member['name']} (Incredible Name: {member['incredible_name']}, Power: {member['power']})")

# Create TheIncredibles object
the_incredibles = TheIncredibles("Incredibles")

# Test the use_power method
try:
    the_incredibles.use_power("Michael")
except Exception as e:
    print(e)

# Call incredible_presentation method
the_incredibles.incredible_presentation()

# Use the born method to add Baby Jack with the following power
the_incredibles.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power')

# Call incredible_presentation method again
the_incredibles.incredible_presentation()
