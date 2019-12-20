from re import *
from Services import Services, generateList
from Complex import ComplexNumber 

class newUI:
    '''
    The commands are
        - "add" value value
        - "list"
        - "filter" startPos endPos
        - "undo"
    '''
    def __init__(self):
        self.numberList = generateList(10)
        self.historyStack = []
    
    def __printComplexNumber(self, com):
        '''
        Prints a complex number in the form (real + i * imag)
        @param:
            - com = ComplexNumber
        @return: 
            - None
        '''
        real = com.Real
        imag = com.Imag
        
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
    
    def __printComplexNumberList(self):
        l = len(self.numberList)
        
        if l == 0:
            print ("List is empty")
        
        else:
            for i in self.numberList:
                self.__printComplexNumber(i)
            print ("")
    
    def __getAdd(self, command):
        '''
        
        '''
        addPattern = r'''
        \ *                             # 0 or more spaces
        (\b add \b)                     # "add" keyword
        \ +                             # 1 or more spaces
        (\d+)                           # 1 or more digits
        \ +                             # 1 or more spaces 
        (\d+)                           # 1 or more digits
        \ *                             # 0 or more spaces
        ,*                              # 1 comma
        '''
        addRegex = compile(addPattern, VERBOSE | IGNORECASE)
        m = match(addRegex, command)
        if m:
            return m.groups()
        
    def __getList(self, command):
        listPattern = r'''
        \ *                             # 0 or more spaces
        (\b list \b)                    # "list" keyword
        \ *                             # 0 or more spaces
        ,*                              # 1 comma
        '''
        listRegex = compile(listPattern, VERBOSE | IGNORECASE)
        m = match(listRegex, command)
        if m:
            return m.groups()
        
    def __getFilter(self, command):
        filterPattern = r'''
        \ *                             # 0 or more spaces
        (\b filter \b)                  # "add" keyword
        \ +                             # 1 or more spaces
        (\d+)                           # 1 or more digits
        \ +                             # 1 or more spaces 
        (\d+)                           # 1 or more digits
        \ *                             # 1 or more spaces
        ,*                              # 1 comma
        '''
        filterRegex = compile(filterPattern, VERBOSE | IGNORECASE)
        m = match(filterRegex, command)
        if m:
            return m.groups()
        
    def __getUndo(self, command):
        undoPattern = r'''
        \ *                             # 0 or more spaces
        (\b undo \b)                    # "undo" keyword
        \ *                             # 0 or more spaces
        ,*                              # 1 comma
        '''
        undoRegex = compile(undoPattern, VERBOSE | IGNORECASE)
        m = match(undoRegex, command)
        if m:
            return m.groups()
    
    def __addUI(self):
        '''
        Interface for the "add" function
        @param:
            - None
        @return:
            - None
        '''
        com = self.__readComplexNumber()
        if com != ComplexNumber(None, None):
            addObj = Services()
            addObj.add(self.numberList, self.historyStack, com)
            
    def __filterUI(self):
        '''
        Interface for the "filter" function
        @param:
            - None
        @return:
            - None
        '''
        #indices should be (startPos, endPos)
        indices = self.__readIndex()

        if tuple != None:
            filterObj = Services()
            filterObj.filter(self.numberList, self.historyStack, indices[0], indices[1])
            
    def __undoUI(self):
        '''
        Interface for the "undo" function
        @param:
            - None
        @return:
            - None
        '''
        undoObj = Services()
        try:
            undoObj.undo(self.numberList, self.historyStack)
        except:
            return
    
    def getInput(self):
        '''
        '''
        x = input("Please insert the commands, separated by a comma: \n")
        i = 0
        l = len(x)
        ServiceObj = Services()
        while i < l:
            if x[i] == 'a':
                command = self.__getAdd(x[i:])
                if command:
                    real = int(command[1])
                    imag = int(command[2])
                    ServiceObj.add(self.numberList, self.historyStack, ComplexNumber(real, imag))
                i += 8
                
            elif x[i] == 'l':
                command = self.__getList(x[i:])
                if command:
                    self.__printComplexNumberList()
                i += 4
                
            elif x[i] == 'f':
                command = self.__getFilter(x[i:])
                if command:
                    startPos = int(command[1])
                    endPos = int(command[2])
                    if startPos < endPos:
                        ServiceObj.filter(self.numberList, self.historyStack, startPos, endPos)
                i += 11
                
            elif x[i] == 'u':
                command = self.__getUndo(x[i:])
                if command:
                    ServiceObj.undo(self.numberList, self.historyStack)
                i += 4
                
            elif x[i] == 'x':
                return -1
            i += 1
        
    def menuInterface(self):
        while True:
            x = self.getInput()
            if x == -1:
                return

