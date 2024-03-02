from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pow(self.radius, 2) * pi

class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return pow(self.side, 2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

def main():
    r = 10
    c = Circle(10)
    print(f"Circle with radius {r} has area of {c.get_area()}")

if __name__=="__main__":
    main()