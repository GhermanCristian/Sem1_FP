#assignment 2 - due on 15 Oct 2019
'''
sequences 
    - 3 = nr. having the same modulus
    - 8 = nr. with (0 <= modulus <= 10)
'''

def parseValue(val):
    #converts a string value to an integer or a floating value
    #atm we assume that 'val' is numerical
    try:
        aux = int(val)
    except:
        aux = float(val)
    return aux

#setter
def setComplexNr(real, imag):
    return (real, imag)

#getters
def getRealPart(com):
    return com[0]
def getImagPart(com):
    return com[1]

def readComplexNr():
    #reads two real numbers, representing the real + imag. part of the nr
    #returns a tuple (real, imag) = the complex number
    
    real, imag = input().split()
    real = parseValue(real)
    imag = parseValue(imag)
    
    return setComplexNr(real, imag)

def printComplexNr(com):
    #prints complex nr;
    #input - a tuple of the form (real, imag)
    #output - complex nr
    real, imag = getRealPart(com), getImagPart(com)
    if imag == 0:
        print (real)
    elif imag == 1:
        print (str(real) + " + i")
    elif imag == -1:
        print (str(real) + " - i")
    else:
        print (str(real) + " + " + str(imag) + "i")    

def displayMenu():
    print ("1. Read a list of complex numbers")
    print ("2. Display the list")
    print ("3. Display list sequences")
    print ("4. Exit program")

def getUserChoice():
    #returns an integer, eventually
    found = False
    while not found:
        x = input("> ")
        try:
            x = int(x)
            if x in range(1, 5):
                found = True
            else:
                print ("No task with this ID. Try again")
        except:
            print ("Value is not an integer. Try again")
    return x

def readList():
    #reads an integer 'n' and 'n' complex numbers;
    #returns a list of tuples
    nrList = []
    
    n = int(input("Please insert 'n': "))
    for i in range(n):
        nrList.append(readComplexNr())
        
    return nrList

def printList(nrList):
    #prints a list of complex numbers, or a message if the list is empty
    print ("")
    if len(nrList) == 0:
        print ("List is empty.")
    else:
        for com in nrList:
            printComplexNr(com)

def modulus(com):
    #returns the square of the modulus of the complex number "com"
    #I use the square in order not to use sqrt and lose some precision
    return getRealPart(com) ** 2 + getImagPart(com) ** 2

'''
def equalModulus(com1, com2):
    #checks if 2 complex numbers have the same modulus
    #returns a boolean value
    return modulus(com1) == modulus(com2)
'''

def firstSequence(nrList):
    #determines the longest list of complex numbers who have the same modulus
    '''
    length = len(nrList)
    pos = 1
    seqLength = 1
    maxLength = 1
    answer = []
    
    while pos < length:
        if equalModulus(nrList[pos - 1], nrList[pos]):
            seqLength += 1
        else:
            if seqLength > maxLength:
                maxLength = seqLength
                answer = nrList[pos - maxLength: pos]
            seqLength = 1
        pos += 1
        
    if seqLength > maxLength:
        answer = nrList[pos - seqLength: pos]
        
    return answer
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
    #checks if the modulus of a complex number is in range [0, 10]
    #returns a boolean value
    return modulus(com) <= 100

def secondSequence(nrList):
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

def main():
    running = True
    nrList = [(0, 0), (1, 2), (2, 1), (-2, 1), (10, 2.2), (10, 2.2), (10, 2.2)]
    while running:
        displayMenu()
        choice = getUserChoice()
        if choice == 1:
            nrList = readList()
        elif choice == 2:
            printList(nrList)
        elif choice == 3:
            printList(firstSequence(nrList))
            printList(secondSequence(nrList))
        elif choice == 4:
            running = False

if __name__ == "__main__":
    main()
    x = "1.2"
    x = float(x)
    print (x)