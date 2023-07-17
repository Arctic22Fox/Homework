import math

class Shape:
    def __init__(self, shape):
        self.shape = shape

    def area(self):
        pass

    def parimeter(self):
        pass

class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

class Cube(Shape):
    def __init__(self, colour, length, width, height):
        super().__init__(colour)
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return self.length * self.width * self.height