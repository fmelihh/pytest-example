import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # pragma: no cover

    @abstractmethod
    def perimeter(self):
        pass  # pragma: no cover


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def __eq__(self, other):
        return self.width == other.width and self.length == other.length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)


class Square(Rectangle):
    def __init__(self, side_length):
        super(Square, self).__init__(side_length, side_length)
