from getData import getImagPart, getRealPart

def modulus(com):
    '''
    Computes the square of the modulus of a complex number. I use the square
    because using sqrt might lose precision
    Input:
        - com = complex number
    Output:
        - square of the modulus of "com"
    '''
    return getRealPart(com) ** 2 + getImagPart(com) ** 2

def firstSequence(nrList):
    '''
    Creates the first sequence (largest with all elements having the same modulus)
    Input:
        - nrList = the entire list of complex numbers
    Output:
        - answer = the longest subsequence with that property
    '''
    length = len(nrList)
    pos = 0
    maxLength = 1
    answer = []
    while pos < length:
        mod = modulus(nrList[pos])
        initPos = pos
        while pos + 1 < length and mod == modulus(nrList[pos + 1]):
            pos += 1
        if pos - initPos + 1 > maxLength:
            maxLength = pos - initPos + 1
            answer = nrList[initPos: pos + 1]
        pos += 1
            
    return answer

def modInRange(com):
    '''
    Checks if the modulus of a complex number is in range [0, 10]
    Input:
        - com = complex number
    Output:
        - a boolean value representing the truthhood of that expression
    '''
    return modulus(com) <= 100

def secondSequence(nrList):
    '''
    Creates the second sequence (largest with all elements : 0 <= modulus(elem) <= 10)
    Input: 
        - nrList = the entire list of complex values
    Output:
        - answer = the longest subsequence with that property
    '''
    length = len(nrList)
    pos = 0
    maxLength = 1
    answer = []
    
    while pos < length:
        while pos < length and not modInRange(nrList[pos]):
            pos += 1
            
        initPos = pos
        while pos < length and modInRange(nrList[pos]):
            pos += 1

        if pos - initPos + 1 > maxLength:
            maxLength = pos - initPos + 1
            answer = nrList[initPos: pos]    
        pos += 1
        
    return answer

def determineDigits(com):
    '''
    Determines the digits (in base 10) of a complex number
    Input:
        - com = complex number of the form (real, imag)
    Output:
        - digits = boolean list, an element is True if that digits exists, False otherwise
    '''
    #empty list
    digits = [False] * 10 
    
    real, imag = abs(getRealPart(com)), abs(getImagPart(com))
    if not isinstance(real, int) or not isinstance(imag, int):
        return None
    
    while real:
        digits[real % 10] = True
        real //= 10
    while imag:
        digits[imag % 10] = True
        imag //= 10
    
    return digits

def sameDigits(com1, com2):
    '''
    Determines if complex values com1 and com2 are written with the same digits (in base 10)
    Input:
        - com1, com2 = complex values of the form (real, imag)
    Output:
        - a boolean value representing the truthhood of that expression
    '''
    return determineDigits(com1) == determineDigits(com2) != None

def thirdSequence(nrList):
    '''
    Creates the third sequence (numbers can be written using the same base-10 digits)
    Input:
        - nrList = the entire list of complex numbers
    Output:
        - answer = the longest subsequence with that property
    '''
    length = len(nrList)
    pos = 0
    maxLength = 1
    answer = []
    
    while pos < length:
        initPos = pos
        
        while pos + 1 < length and sameDigits(nrList[pos], nrList[pos + 1]):
            pos += 1
            
        if pos - initPos + 1 > maxLength:
            maxLength = pos - initPos + 1
            answer = nrList[initPos: pos + 1]
        pos += 1
            
    return answer
