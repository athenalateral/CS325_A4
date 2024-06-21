'''
Filename: l.py
Author: Ethan Lemieux
Purpose: Demonstrate the Liskov Substitution Principle (LSP)

'''

from abc import ABC, abstractmethod
import math

PI = math.pi

class Shape(ABC):
    @abstractmethod
    def set_width(self):
        raise NotImplementedError("Subclass must implement set_width")

    def set_height(self):
        raise NotImplementedError("Subclass must implement set_height")

    def calc_area(self):
        raise NotImplementedError("Subclass must implement calc_area")
    
# Shape classes

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def set_width(self, width):
        #functionality
        pass

    def set_height(self, height):
        #functionality
        pass

    def calc_area(self):
        return PI * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.length = height

    def calc_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def set_width(self, width):
        self.base = width

    def set_height(self, height):
        self.height = height

    def calc_area(self):
        return 1/2.0 * self.base * self.height

# Base functionality that can be used or not dependant on class

def set_width(shape, width):
    if isinstance(shape, Shape):
        shape.set_width(width)
    else:
        print("This Shape does not use width")

def set_height(shape, height):
    if isinstance(shape, Shape):
        shape.set_height(height)
    else:
        print("This Shape does not use height")

def calc_area(shape):
    if isinstance(shape, Shape):
        shape.calc_area()


