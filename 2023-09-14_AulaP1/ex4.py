#!/usr/bin/env python3

maximum_number = 100000

def getDividers(value):
    dividers = []
    
    for i in range(1,value):
        if value % i == 0:
            dividers.append(i)
    
    return dividers

def isPerfect(value):
    if value <= 0:
        return False
    
    divisors_sum = 0
    for i in range(1, value):
        if value % i == 0:
            divisors_sum += i

    return divisors_sum == value


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')
            dividers = getDividers(i)
            print('Divisores: ' + str(dividers))


if __name__ == "__main__":
    main()