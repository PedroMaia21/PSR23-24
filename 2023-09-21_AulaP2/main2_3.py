#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
import argparse

from colorama import Fore, Back, Style
from my_functions import isPrime

# define functions here ...

def main():
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers')
    parser.add_argument('-mn', '--maximun_number', type=int, help='max number.', required=True)

    args = vars (parser.parse_args())


    print("Starting to compute prime numbers up to " + str(args['maximun_number']))

    for i in range(2, args['maximun_number']): # for cycle to go from o to number chosen
        if isPrime(i):
            print('Number ' + Fore.GREEN + str(i) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + Fore.RED + str(i) + ' is not prime.' + Style.RESET_ALL)

    printAllPreviousChars()

if __name__ == "__main__":
    main()