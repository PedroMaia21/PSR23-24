#!/usr/bin/env python3

from colorama import Fore, Back, Style
from collections import namedtuple


class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        realPart = self.r + y.r
        imaginaryPart = self.i + y.i
        complexTuple = Complex(realPart,imaginaryPart)
        return complexTuple

    def multiply(self, y):
        realPart = self.r * y.r - self.i * y.i
        imaginaryPart = self.r * y.i + self.i * y.r
        complexTuple = Complex(realPart,imaginaryPart)
        return complexTuple

    def __str__(self):
        realPart = self.r
        imaginaryPart = self.i
        if imaginaryPart>=0:
            return 'Complex Number: '+str(realPart)+'+'+str(imaginaryPart)+'i'
        else:
            return 'Complex Number: '+str(realPart)+'-'+str(imaginaryPart)+'i'

c1 = Complex(5, 3)
print(c1)

c2 = Complex(-2, 7)
print(c2)

# Test add
c3 = c1.add(c2)
print(c3)

c4=c2.add(c3)
print(c4)

# test multiply
print(c1.multiply(c2))

