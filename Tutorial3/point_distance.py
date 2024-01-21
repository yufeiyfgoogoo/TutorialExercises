import math

class Point():
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def distance_to_origin(self):
        """input the coordinate value of a point and return the distance between the point and origin"""
        return math.sqrt(self.x ** 2 + self.y ** 2)




