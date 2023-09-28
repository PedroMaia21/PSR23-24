#!/usr/bin/env python3

from colorama import Fore, Back, Style
from time import time, ctime

from collections import namedtuple
import math

def addComplex(x, y):
    realPart = x.real + y.real
    imaginaryPart = x.imag + y.imag
    complexTuple = Complex(realPart,imaginaryPart)
    return complexTuple

def multiplyComplex(x, y):
    realPart = (x.real * y.real) - (x.imag * y.imag)
    imaginaryPart = (x.real * y.imag) + (x.imag * y.real)
    complexTuple = Complex(realPart,imaginaryPart)
    return complexTuple


def printComplex(x):
    realPart = x.real
    imaginaryPart = x.imag

    print('Complex Number: '+str(realPart)+'+'+str(imaginaryPart)+'i')

Complex=namedtuple('Complex',['real','imag'])

c1 = Complex(5, 3)
print(c1)

c2 = Complex(-2, 7)
print(c2)

# Test add
c3 = addComplex(c1, c2)
print(c3)

c4=addComplex(c2,c3)
print(c4)

# test multiply
printComplex(multiplyComplex(c1, c2))
