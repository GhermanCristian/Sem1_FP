#getters
def getRealPart(com):
    return com[0]
def getImagPart(com):
    return com[1]

def printComplexNr(com):
    '''
    Prints a complex number in the form "a + ib"
    Input:
        - com = tuple of the form (real, imag)
    Output:
        - prints a complex number on the console
    '''
    real, imag = getRealPart(com), getImagPart(com)
    if imag == 0:
        print (real)
    elif imag == 1:
        print (str(real) + " + i")
    elif imag == -1:
        print (str(real) + " - i")
    elif imag < 0:
        print (str(real) + " " + str(imag) + "i")
    else:
        print (str(real) + " + " + str(imag) + "i")
        
def printList(nrList):
    '''
    Prints a list of complex numbers, or a message if the list is empty
    Input:
        - nrList = list of complex numbers
    Output:
        - prints a list of complex number in the console or an error message
    '''
    print ("")
    if len(nrList) == 0:
        print ("List is empty.")
    else:
        for com in nrList:
            printComplexNr(com)
    print ("")