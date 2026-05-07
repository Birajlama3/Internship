# Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        a = math.pi * self.radius**2
        return a

    def perimeter(self):
        p = 2 * math.pi * self.radius
        return p
c = Circle(7)
print(c.area())
print(c.perimeter()) 