from Complex import ComplexNumber
from Services import Services, generateList

class UI:    
    def __init__(self):
        self.numberList = generateList(10)
        self.historyStack = []
    
    def __readCommand(self):
        '''
        Reads command from console
        @param:
            - None
        @return:
            - commandID (integer), if the input is valid
            - None, otherwise
        '''
        commandID = input("\nPlease insert a command: ")
        try:
            commandID = self.__validateInput(commandID)
            if commandID < 0 or commandID > 4:
                raise ValueError("Invalid command ID")
        except:
            return None
        
        return commandID
    
    def menuInterface(self):
        '''
        Executes commands from the user
        @param:
            - None
        @return:
            - None
        '''
        print ("""
            0. Exit
            1. Add a number to the list (the number is read from the console)
            2. Print the complex number list
            3. Filter list so that it only contains the elements between the indices startPos, endPos (read from the console)
            4. Undo
        """)
        while True:
            commandID = self.__readCommand()
            
            if commandID == None:
                continue
            
            if commandID == 0:
                print ("Program has ended.")
                return
            
            if commandID == 1:
                self.__addUI()
            elif commandID == 2:
                self.__printComplexNumberList()
            elif commandID == 3:
                self.__filterUI()
            elif commandID == 4:
                self.__undoUI()
        
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
      
    def __hasLetters(self, val):
        '''
        Determines if "val" contains alphabetic characters
        @param:
            - val = string
        @return:
            - True, if val contains letters
            - False, otherwise
        '''
        for i in val:
            if i.isalpha():
                return True
        return False
        
    def __validateInput(self, val):
        '''
        Checks if "val" is a valid number (integer of float)
        @param:
            - val = value to be evaluated (string)
        @return:
            - None, if val is invalid
            - val (as an integer of float), otherwise
        '''
        if self.__hasLetters(val) == True:
            raise TypeError("NaN")
        
        try:
            aux = int(val)
        except:
            aux = float(val)
        
        return aux
    
    def __readComplexNumber(self):
        '''
        Reads a ComplexNumber from the console
        @param:
            - None
        @return:
            - ComplexNumber, if the input was valid
            - None, otherwise
        '''
        try:
            real, imag = input("Please insert real and imaginary part: ").split()
            real = self.__validateInput(real)
            imag = self.__validateInput(imag)
        except:
            print ("Invalid complex number")
            return None
        
        return ComplexNumber(real, imag)
    
    def __readIndex(self):
        '''
        Reads startPos and endPos from the console
        @param:
            - None
        @return:
            - tuple containing startPos and endPos (integers, startPos <= endPos), if the input is valid
            - None, otherwise
        '''
        try:
            startPos, endPos = input("Please insert startPos and endPos: ").split()
            startPos = self.__validateInput(startPos)
            endPos = self.__validateInput(endPos)
            if startPos > endPos:
                raise ValueError("Start position is larger than end position")
        
        except:
            return None
        
        return (startPos, endPos)
     
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


