import math
# test Shape
def calculate_area(self):
    """an abstract function to calculate the area"""
    pass

def test_calculate_area():
    pass

def calculate_perimeter(self):
    """an abstract function to calculate the perimeter"""
    pass

def test_calculate_perimeter():
    pass


# test triangle
def calculate_area(base, height):
    """input the base and height of the triangle and output the area"""
    return 0.5 * base * height

def test_calculate_area():
    assert calculate_area(2, 2) == 2

def calculate_perimeter(side1, side2, side3):
    """input 3 sides of the triangle and output the perimeter"""
    return side1 + side2 + side3

def test_calculate_perimeter():
    assert calculate_perimeter(1, 1, 1) == 3

# test square

def calculate_area(side):
    """input the side of the square and output the area"""
    return side ** 2

def test_calculate_area():
    assert calculate_area(2) == 4

def calculate_perimeter(side):
    """input the side of the square and output the perimeter"""
    return 4 * side

def test_calculate_perimeter():
    assert calculate_perimeter(1) == 4

# test rectangle
def calculate_area(length, width):
    """input the length and width of the rectangle and output the area"""
    return length * width

def test_calculate_area():
    assert calculate_area(2, 3) == 6

def calculate_perimeter(length, width):
    """input the length and width of the rectangle and output the perimeter"""
    return 2 * (length + width)

def test_calculate_perimeter():
    assert calculate_perimeter(2, 3) == 10

# test circle
def calculate_area(radius):
    """input the radius of the circle and output the area"""
    return math.pi * radius ** 2

def test_calculate_area():
    assert calculate_area(3) == 28.274333882308138

def calculate_perimeter(radius):
    """input the radius of the circle and output the perimeter"""
    return 2 * math.pi * radius

def test_calculate_perimeter():
    assert calculate_perimeter(3) == 18.84955592153876

# test cylinder
def calculate_area(radius, height):
    """input the area of the circle and height of the cylinder then output the area of the cylinder"""
    return 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height

def test_calculate_area():
    assert calculate_area(2, 3) == 62.83185307179586