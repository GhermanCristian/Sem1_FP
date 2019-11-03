from Services import Services
from Complex import ComplexNumber

class Test(Services):
    def __testAdd(self):
        '''
        Test the 'add' function
        '''
        numberList = []
        historyStack = []
        
        self.add(numberList, historyStack, ComplexNumber(5, 6))
        self.add(numberList, historyStack, ComplexNumber(10, 2))
        self.add(numberList, historyStack, ComplexNumber(5.4, 6.7))
        self.add(numberList, historyStack, ComplexNumber(101, 21))
        self.add(numberList, historyStack, ComplexNumber(-5.41, -6.71))
        assert len(numberList) == 5
        assert numberList[0] == ComplexNumber(5, 6)
        assert numberList[1] == ComplexNumber(10, 2)
        assert numberList[2] == ComplexNumber(5.4, 6.7)
        assert numberList[3] == ComplexNumber(101, 21)
        assert numberList[4] == ComplexNumber(-5.41, -6.71)
    
    def __testFilter(self):
        '''
        Test the 'filter' function
        '''
        numberList = []
        historyStack = []
        
        self.add(numberList, historyStack, ComplexNumber(5, 6))
        self.add(numberList, historyStack, ComplexNumber(10, 2))
        self.add(numberList, historyStack, ComplexNumber(5.4, 6.7))
        self.add(numberList, historyStack, ComplexNumber(101, 21))
        self.add(numberList, historyStack, ComplexNumber(-5.41, -6.71))
        
        self.filter(numberList, historyStack, 0, 1)
        assert len(numberList) == 2
        assert numberList[0] == ComplexNumber(5, 6)
        assert numberList[1] == ComplexNumber(10, 2)
        
        numberList = []
        historyStack = []
        
        self.add(numberList, historyStack, ComplexNumber(5, 6))
        self.add(numberList, historyStack, ComplexNumber(10, 2))
        self.add(numberList, historyStack, ComplexNumber(5.4, 6.7))
        self.add(numberList, historyStack, ComplexNumber(101, 21))
        self.add(numberList, historyStack, ComplexNumber(-5.41, -6.71))
        self.filter(numberList, historyStack, 1, 3)
        assert len(numberList) == 3
        assert numberList[0] == ComplexNumber(10, 2)
        assert numberList[1] == ComplexNumber(5.4, 6.7)
        assert numberList[2] == ComplexNumber(101, 21)

    def __testUndo(self):
        '''
        Test the 'undo function
        '''
        numberList = []
        historyStack = []
        
        self.add(numberList, historyStack, ComplexNumber(5, 6))
        self.add(numberList, historyStack, ComplexNumber(10, 2))
        self.undo(numberList, historyStack)
        assert len(numberList) == 1
        assert numberList[0] == ComplexNumber(5, 6)
        
        self.add(numberList, historyStack, ComplexNumber(5.4, 6.7))
        self.add(numberList, historyStack, ComplexNumber(101, 21))
        self.add(numberList, historyStack, ComplexNumber(-5.41, -6.71))
        self.undo(numberList, historyStack)
        assert len(numberList) == 3
        assert numberList[0] == ComplexNumber(5, 6)
        assert numberList[1] == ComplexNumber(5.4, 6.7)
        assert numberList[2] == ComplexNumber(101, 21)
        
        self.add(numberList, historyStack, ComplexNumber(-5.41, -6.71))
        self.filter(numberList, historyStack, 0, 2)
        self.undo(numberList, historyStack)
        assert len(numberList) == 4
        assert numberList[0] == ComplexNumber(5, 6)
        assert numberList[1] == ComplexNumber(5.4, 6.7)
        assert numberList[2] == ComplexNumber(101, 21)
        assert numberList[3] == ComplexNumber(-5.41, -6.71)
        
        self.filter(numberList, historyStack, 0, 1)
        self.undo(numberList, historyStack)
        assert len(numberList) == 4
        assert numberList[0] == ComplexNumber(5, 6)
        assert numberList[1] == ComplexNumber(5.4, 6.7)
        assert numberList[2] == ComplexNumber(101, 21)
        assert numberList[3] == ComplexNumber(-5.41, -6.71)

    def testFunction(self):
        self.__testAdd()
        self.__testFilter()
        self.__testUndo()


