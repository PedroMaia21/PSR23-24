#!/usr/bin/env python3

from colorama import Fore, Back, Style
from time import time, ctime
from function_lib import addComplex, multiplyComplex, printComplex
from collections import namedtuple
import math

seconds = time()

value = 50

for i in range(1,value):
    r = math.sqrt(i)


now = time()
secondsPassed = now-seconds
localTime = ctime(now)

print('Hora Atual: '+localTime)
print('Segundos que passaram durante o processamento: '+Fore.LIGHTCYAN_EX+str(secondsPassed)+Style.RESET_ALL)



c1 = (5, 3)
c2 = (-2, 7)

# Test add
c3 = addComplex(c1, c2)
printComplex(c3)

# test multiply
printComplex(multiplyComplex(c1, c2))
