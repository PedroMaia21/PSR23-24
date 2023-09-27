def addComplex(x, y):
    realPart = x[0]+y[0]
    imaginaryPart = x[1]+y[1]
    complexTuple = (realPart,imaginaryPart)
    return complexTuple

def multiplyComplex(x, y):
    realPart = (x[0]*y[0])-(x[1]*y[1])
    imaginaryPart = (x[0]*y[1])+(x[1]*y[0])
    complexTuple = (realPart,imaginaryPart)
    return complexTuple


def printComplex(x):
    realPart = x[0]
    imaginaryPart = x[1]

    print('Complex Number: '+str(realPart)+'+'+str(imaginaryPart)+'i')