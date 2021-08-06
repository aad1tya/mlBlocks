import math

class Point:
    def __init__(self, x = 0, y = 0):
        """Initializes the position of a new point. The x and y
           coordinates can be specified. If not specified, they
           will get defaulted to 0"""
        self.move(x, y)

    def move(self, x, y):
        """Move a point in the 2D space using x and y values"""
        self.x = x
        self.y = y

    def reset(self):
        """Reset the points to zero aka the origin"""
        self.move(0, 0)
    
    def calculate_distance(self, other_point):
        """Calculates the distance between two points using the
           Pythagorean Theorem. The return value is a float.
           
           Parameters:
           other_point = The passed value should be an object instantiated
                         from a class"""
        return math.sqrt(
            (self.x - other_point.x)**2
            +    (self.y - other_point.y)**2
        )

point1 = Point(4, 3)
point2 = Point(-2, 4)

assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

print(point1.calculate_distance(point2))