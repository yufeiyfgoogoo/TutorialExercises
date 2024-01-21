import math
import pytest
# Define a base class called Shape to represent a generic shape with methods for calculating area and perimeter
class Shape:
    def calculate_area(self):
        """an abstract function to calculate the area"""
        pass

    def calculate_perimeter(self):
        """an abstract function to calculate the perimeter"""
        pass

# Define a derived class called Triangle, which inherits from the Shape class
class Triangle(Shape):
    # Initialize the Triangle object with a base, height, and three side lengths
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Calculate and return the area of the triangle using the formula: 0.5 * base * height
    def calculate_area(self):
        """input the base and height of the triangle and output the area"""
        return 0.5 * self.base * self.height

    # Calculate and return the perimeter of the triangle by adding the lengths of its three sides
    def calculate_perimeter(self):
        """input 3 sides of the triangle and output the perimeter"""
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    # Initialize the Rectangle object with given length and width
    def __init__(self, side):
        self.side = side

    # Calculate and return the area of the rectangle using the formula: length * width
    def calculate_area(self):
        """input the side of the square and output the area"""
        return self.side ** 2

    # Calculate and return the perimeter of the rectangle using the formula: 2 * (length + width)
    def calculate_perimeter(self):
        """input the side of the square and output the perimeter"""
        return 4 * self.side

# Define a derived class called Rectangle, which inherits from the Shape class
class Rectangle(Shape):
    # Initialize the Rectangle object with given length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculate and return the area of the rectangle using the formula: length * width
    def calculate_area(self):
        """input the length and width of the rectangle and output the area"""
        return self.length * self.width

    # Calculate and return the perimeter of the rectangle using the formula: 2 * (length + width)
    def calculate_perimeter(self):
        """input the length and width of the rectangle and output the perimeter"""
        return 2 * (self.length + self.width)

# Define a derived class called Circle, which inherits from the Shape class
class Circle(Shape):
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius

    # Calculate and return the area of the circle using the formula: π * r^2
    def calculate_area(self):
        """input the radius of the circle and output the area"""
        return math.pi * self.radius ** 2

    # Calculate and return the perimeter of the circle using the formula: 2π * r
    def calculate_perimeter(self):
        """input the radius of the circle and output the perimeter"""
        return 2 * math.pi * self.radius

class Cylinder(Circle):
    def __init__(self, radius, height):
        Circle.__init__(self, radius)
        self.height = float(height)

    def calculate_area(self):
        """input the area of the circle and height of the cylinder then output the area of the cylinder"""
        return 2 * Circle.area(self) + 2 * math.pi * self.radius * self.height



