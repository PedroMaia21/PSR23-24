#!/usr/bin/env python
#shebang line to inform the OS that the content its in python

from colorama import Fore, Back, Style

#Exercice 3

maximum_number = 10000


def isPrime(value):
    if value <= 1:
        return False
    elif value <= 3:
        return True
    elif value % 2 == 0 or value % 3 == 0:
        return False
    a=5
    while a * a <= value:
        if value % a == 0 or value % (a+2) == 0:
            return False
        a += 6
    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()