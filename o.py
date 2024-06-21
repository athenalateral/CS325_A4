'''
Filename: o.py
Author: Ethan Lemieux
Purpose: Demonstrate the Open-Closed Principle (OCP)

'''

from abc import ABC, abstractmethod
import math

PI = math.pi

class CalcArea(ABC):
    @abstractmethod
    def calc_area(self):
        pass

class Quadrelateral(CalcArea):
    def calc_area(self, length, width):
        area = length * width
        print("Area: " + area)

class Circle(CalcArea):
    def calc_area(self, radius):
        area = 2 * PI * radius * radius
        print ("Area: " + area)

class Triangle(CalcArea):
    def calc_area(self, base, width):
        area = 1/2.0 * base * width
        print ("Area: " + area)

class Shape:
    def __init__(self, unit_A, unit_B, unit_C):
        self.unit_A = unit_A
        self.unit_B = unit_B
        self.unit_C = unit_C

    def calc_area(self, area_calculator):
        area_calculator.calc_area(self, self.unit_A, self.unit_B, self.unit_C)