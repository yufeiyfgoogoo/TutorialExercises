import math
def line_length(beginning_x, beginning_y, end_x, end_y):
    """input two coordinate of x and y then output the length of the line"""
    sum_of_squares = (end_x - beginning_x) ** 2 + (end_y - beginning_y) ** 2
    return math.sqrt(sum_of_squares)

def test_line_length():
    assert line_length(1, 2, 3, 4) == 2.8284271247461903