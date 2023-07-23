import math
import random
# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

class Circle:
    def __init__(self, radius = "1.0"):
        self.radius = float(input("Give me a radius of a circle: "))
    
    def area(self):
        return 2 * math.pi * self.radius

    def perimeter(self):
        return math.pi * self.radius ** 2

    def print_results(self):
        print(f"A circle is a closed shape with all points equidistant from the center point. It is defined by its radius, which is {self.radius} units.")

circle1 = Circle()

print("Perimeter:", circle1.perimeter())
print("Area:", circle1.area())



# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).

class MyList:
    def __init__(self,letters):
        self.mylist = letters
    
    def reversed_lists(self):
        return list(reversed(self.mylist))
    
    def sorting_list(self):
        return sorted(self.mylist)
    
    def extra_list(self):
        return [random.randint(1, 100)for _ in range(len(self.mylist))]
       
    
letters_list = ['a', 'b', 'c', 'd', 'e']
my_list_object = MyList(letters_list)

reversed_list = my_list_object.reversed_lists()
print("Reversed List:", reversed_list)

# Get the sorted list
sorted_list = my_list_object.sorting_list()
print("Sorted List:", sorted_list)

# Generate a second list with random numbers
random_list = my_list_object.extra_list()
print("Random List:", random_list)

    
# Exercise 3 : Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

# Create a python file called menu_manager.py.

# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).

# Here is a list of the dishes currently on the menu:

#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True

#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# The dishes provided above should be the value of the menu attribute.

# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.

# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.

# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.