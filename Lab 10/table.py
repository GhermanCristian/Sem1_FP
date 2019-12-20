from customExceptions import RangeError
from constants import EMPTY_SYMBOL

class Table(object):
    def __init__(self, boardWidth, boardHeight):
        self.__width = boardWidth
        self.__height = boardHeight
        
        self.__table = []
        for i in range(boardHeight):
            aux = []
            for j in range(boardWidth):
                aux.append(EMPTY_SYMBOL)
            self.__table.append(aux)
        
        self.__cells = boardHeight * boardWidth
        
    def getValue(self, xCoord, yCoord):
        '''
        Returns the value of the table at given coordinates
        @param:
            - xCoord, yCoord = integers
        @return:
            - value of the table at given coordintates, if they are valid
        @raise:
            - RangeError, if the coordinates are outside of the table
        '''
        if xCoord < 0 or yCoord < 0 or xCoord >= self.__height or yCoord >= self.__width:
            raise RangeError("Position outside of the table")
        return self.__table[xCoord][yCoord]
    
    def setValue(self, xCoord, yCoord, value):
        '''
        Modifies the value of the table at given coordinates
        @param:
            - xCoord, yCoord = integers
            - value = character
        @return:
            - None
        @raise:
            - None
        '''
        if xCoord >= 0 and yCoord >= 0 and xCoord < self.__height and yCoord < self.__width:
            if self.__table[xCoord][yCoord] == EMPTY_SYMBOL:
                self.__cells -= 1
            self.__table[xCoord][yCoord] = value
        
    def isFull(self):
        '''
        Checks if the current table is full (no cells filled with the EMPTY_SYMBOL)
        @param:
            - None
        @return:
            - True, if the table is full
            - False, otherwise
        @raise:
            - None
        '''
        return self.__cells == 0
    
    def getFirstEmpty(self):
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__table[i][j] == EMPTY_SYMBOL: 
                    return (i, j)   
                
    def getAllEmpty(self):
        auxList = []
        
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__table[i][j] == EMPTY_SYMBOL:
                    auxList.append((i, j))
                    
        return auxList
                
    def getPrintable(self):
        return self.__table

