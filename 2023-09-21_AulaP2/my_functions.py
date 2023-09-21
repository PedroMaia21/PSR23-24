import readchar

def isPrime(value):
    for i in range(2,round(value/2)+1):
        if value%i == 0:
            return False

    return True

def printAllPreviousChars():
    stringChars=''

    print('Press a key to generate a char string')
    
    key = readchar.readkey()
    numberChar = ord(key)

    for i in range(32,numberChar):
        stringChars += chr(i)
    print('The string is: '+stringChars)

def readAllUpTo(stopChar):
    print('Write your secret string. to end press '+stopChar)
    persString=''
    while True:
        key = readchar.readkey()

        if key == stopChar:
            break

        persString += key
    print('Your string is: ' + persString)
        
def countNumbersUpTo(stopChar):
    print('Press random keys. To end press '+stopChar)

    total_numbers = 0
    total_others = 0
    while True:
        key = readchar.readkey()

        if key == stopChar:
            break        
        
        if key.isnumeric():
            total_numbers+=1
        else:
            total_others+=1

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')