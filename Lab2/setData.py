#setter
def setComplexNr(real, imag):
    return (real, imag)

def hasLetters(val):
    '''
    Determines if "val" contains alphabetic characters
    Input:
        - val = string
    Output:
        - boolean value = truthhood of that expression
    '''
    for i in val:
        if i.isalpha():
            return True
    return False

def parseValue(val):
    '''
    Converts a string value to an integer or a floating value.
    Because of "hasLetters" we know that it does not contain letters
    Input:
        - val = string which represents a numerical value
    Output:
        - aux = integer of floating value
    '''
    try:
        aux = int(val)
    except:
        aux = float(val)
    return aux

def readComplexNr():
    '''
    Reads from the console two strings which should represent real numbers (the real and
    the imaginary part of a complex number)
    Input:
        - None
    Output:
        - a tuple which represents a complex number
    '''
    while True:
        real, imag = input().split()
        if not (hasLetters(real) or hasLetters(imag)):
            real = parseValue(real)
            imag = parseValue(imag)
            break
        print ("Error. This is an alphabetic character. Try again")
    
    return setComplexNr(real, imag)

def readList():
    '''
    Reads from the console an integer 'n' and 'n' complex numbers
    Input:
        - None
    Output:
        - nrList = a list of 'n' complex numbers, which are represented as tuples
    '''
    nrList = []
    
    while True:
        n = input("Please insert 'n': ")
        if n.isnumeric() == True:
            n = int(n)
            break
        print ("This is not an integer. Try again")
    
    for i in range(n):
        nrList.append(readComplexNr())
        
    return nrList
