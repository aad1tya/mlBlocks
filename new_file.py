import math

class Point:
    def __init__(self, x, y):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)
    
    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 +
                (self.y - other_point.y)**2
        )

point1 = Point(4, 3)
point2 = Point(-2, 4)

assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

print(point1.calculate_distance(point2))