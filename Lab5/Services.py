'''
 Module for the Services class (implementation of required functionalities)
'''

class Services:
    '''
    Class for the "add", "filter", "undo" functionalities
    We assume that all input is valid
    '''
    
    def add(self, numberList, historyStack, com):
        '''
        Adds a complex number to the end of numberList
        @param:
            - numberList = list of complex numbers
            - com = ComplexNumber
            - historyStack = list (organised as a stack) which contains the LPOs and their arguments
        @return:
            - None
        '''
        historyStack.append((1, []))
        numberList.append(com)
        
    def __addReverse(self, numberList, argList):
        '''
        Reverse operation of 'add'
        @param:
            - numberList = list of complex numbers
            - argList = list of the LPO's arguments (in this case is not used)
        @return:
            - None
        '''
        numberList.pop()
        
    def filter(self, numberList, historyStack, startPos, endPos):
        '''
        Filters a list so that it only contains the values between indices startPos and endPos
        @param:
            - numberList = list of complex numbers
            - startPos = integer, starting position of the range
            - endPos = integer, end position of the range
            - historyStack = list (organised as a stack) which contains the LPOs and their arguments
        @return:
            - None
        '''
        firstSection = numberList[:startPos]
        secondSection = numberList[endPos + 1: ]
        historyStack.append((2, [firstSection, secondSection]))
        
        auxList = numberList[startPos : endPos + 1]
        numberList.clear()
        numberList.extend(auxList)
        
    def __filterReverse(self, numberList, argList):
        '''
        Reverse operation of 'filter'
        @param:
            - numberList = list of complex numbers
            - argList = list of the LPO's arguments (in this case is not used)
        @return:
            - None
        '''
        firstSection = argList[0]
        secondSection = argList[1]
        
        aux = numberList[:]
        numberList.clear()
        numberList.extend(firstSection)
        numberList.extend(aux)
        numberList.extend(secondSection)
        
    def undo(self, numberList, historyStack):
        '''
        Undoes the LPO (last performed operation)
        @param:
            - numberList = list of complex numbers
            - historyStack = list (organised as a stack) which contains the LPOs and their arguments
        @return:
            - None
        '''
        l = len(historyStack)
        
        if l == 0:
            raise IndexError("No more undo's left")
        
        LPO = historyStack.pop()
        commandID = LPO[0]
        argList = LPO[1]
        
        if commandID == 1:
            self.__addReverse(numberList, argList)
            
        elif commandID == 2:
            self.__filterReverse(numberList, argList)

        #the program should never reach this point, but just in case
        else:
            raise ValueError("Invalid command ID")

def generateList(n):
    '''
    Randomly generates a list of 'n' complex numbers
    @param:
        - n = integer
    @return:
        - numberList = randomly generated list of complex numbers
    '''
    import random
    from Complex import ComplexNumber
        
    numberList = []
        
    for i in range(n):
        numberList.append(ComplexNumber(random.randint(0, 100), random.randint(0, 100)))
            
    return numberList


