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
        
        #the number of empty cells
        self.__emptyCells = boardHeight * boardWidth
        
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
            - RangeError, if the coordinates are outside of the table
        '''
        if xCoord < 0 or yCoord < 0 or xCoord >= self.__height or yCoord >= self.__width:
            return
            
        if self.__table[xCoord][yCoord] == EMPTY_SYMBOL and value != EMPTY_SYMBOL:
            self.__emptyCells -= 1
        #used when restoring the table
        elif self.__table[xCoord][yCoord] != EMPTY_SYMBOL and value == EMPTY_SYMBOL:
            self.__emptyCells += 1

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
        return self.__emptyCells == 0
    
    def getFirstEmpty(self):
        '''
        Gets the first empty position in the table (we are sure that one exists)
        @param:
            - None
        @return:
            - tuple containing the coordinates
        @raise:
            - None
        '''
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__table[i][j] == EMPTY_SYMBOL: 
                    return (i, j)   
                
    def getAllEmpty(self):
        '''
        Gets all the empty positions in the table (we are sure that at least one exists)
        @param:
            - None
        @return:
            - list of tuples, each containing the coordinates
        @raise:
            - None
        '''
        auxList = []
        
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__table[i][j] == EMPTY_SYMBOL:
                    auxList.append((i, j))
                    
        return auxList
                
    def content(self):
        return self.__table
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    #only used in testing
    @property
    def emptyCells(self):
        return self.__emptyCells

