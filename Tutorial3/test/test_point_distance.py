import math

def distance_to_origin(x, y):
    """input the coordinate value of a point and return the distance between the point and origin"""
    return math.sqrt(x ** 2 + y ** 2)

def test_point_distance():
    assert distance_to_origin(1, 1) == 1.4142135623730951
