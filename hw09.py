"""
Write Abstract class Figure
Inherit Triangle and Circle from it
Create a collection of Figures, count perimeter and square of them
"""

from abc import abstractmethod
import math
import random


class Figure:

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

    def get_square(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        square = math.sqrt(semi_perimeter * (semi_perimeter - self.side_a) * (semi_perimeter - self.side_b) * (semi_perimeter - self.side_c))
        return square


class Circle(Figure):

    def __init__(self, radius_of_circle):
        self.radius_of_circle = radius_of_circle

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius_of_circle
        return perimeter

    def get_square(self):
        square = math.pi * self.radius_of_circle**2
        return square


tri01 = Triangle(15, 12, 10)
circ01 = Circle(15)

list_of_figures = [tri01, circ01]

for i in range(1, 10):
    i = Triangle(random.randrange(7, 15), random.randrange(7, 12), random.randrange(10, 15))
    list_of_figures.append(i)
    i = Circle(random.randrange(5, 15))
    list_of_figures.append(i)

print(list_of_figures)

for figure in list_of_figures:
    if isinstance(figure, Triangle):
        print(f"Triangle perimeter is {figure.get_perimeter()} and square is {figure.get_square()}")
    elif isinstance(figure, Circle):
        print(f"Circle perimeter is {figure.get_perimeter()} and square is {figure.get_square()}")
