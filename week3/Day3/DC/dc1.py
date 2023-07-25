# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together - use a dunder method
# Be able to compare two circles to see which is bigger - use a dunder method
# Be able to compare two circles and see if there are equal - use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            f"Either radius or diameter must be specified."
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

if __name__ == "__main__":
    circle1 = Circle(radius=5)
    circle2 = Circle(diameter=8)
    print(circle1)  # Output: Circle with radius 5
    print(circle2)  # Output: Circle with radius 4.0 (diameter of 8 / 2)

    print(circle1.diameter)  # Output: 10
    print(circle2.diameter)  # Output: 8

    print(circle1.area)  # Output: 78.53981633974483
    print(circle2.area)  # Output: 50.26548245743669

    circle3 = circle1 + circle2
    print(circle3)  # Output: Circle with radius 9.0 (sum of radii)

    circles = [circle1, circle2, circle3]
    circles.sort()
    for circle in circles:
        print(circle)
