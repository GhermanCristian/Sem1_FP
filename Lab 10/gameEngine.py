import random
from table import Table
from customExceptions import EmptyError, RangeError
from constants import *

class GameEngine(object):
    def __init__(self, player, boardWidth, boardHeight):
        if player == 0:
            self.__player = random.randint(1,2)
        else:
            self.__player = player
            
        self.__table = Table(boardWidth, boardHeight)
        
    def __move(self, xCoord, yCoord, value):
        '''
        Performs a move on the table, at given coordinates
        @param:
            - xCoord, yCoord - integers, valid
            - value - character
        @return:
            - None
        @raise:
            - EmptyError, if the position is not empty
        '''
        if self.__table.getValue(xCoord, yCoord) != EMPTY_SYMBOL:
            raise EmptyError("Position is not empty")
        
        if xCoord < 0 or yCoord < 0 or xCoord >= self.__table.height or yCoord >= self.__table.width:
            raise RangeError("Position outside of the table")
        
        for i in range(xCoord - 1, xCoord + 2):
            for j in range(yCoord - 1, yCoord + 2):
                self.__table.setValue(i, j, OCCUPIED_SYMBOL)    
        
        self.__table.setValue(xCoord, yCoord, value)     
        
    def playerMove(self, xCoord, yCoord):
        '''
        Performs a player move
        @param:
            - xCoord, yCoord - integers, the coordinates given by the user (valid)
        @return:
            - PLAYER_SYMBOL = character, if the player has won
            - COMPUTER_SYMBOL = character, if the computer has won
            - None, if the game is not over
        @raise:
            - EmptyError, if the position is not empty
        '''
        #the player cannot move, thus the computer has won
        if self.__table.isFull() == True:
            return COMPUTER_SYMBOL
        
        self.__move(xCoord, yCoord, PLAYER_SYMBOL)
    
    def __processEmptyArea(self, x, y):
        '''
        Traverses all the cells in an empty area (they have to be connected in 1 of the 8 directions)
        @param:
            - x, y = integers, initial coordinates
        @return:
            - tileCount = integer, nr of tiles
            - xMax, xMin, yMax, yMin = max / min bounds of the area
            - sumX, sumY = sum of the x / y coordinates
        @raise:
            - None
        '''
        #BFS
        #the first position is the one consisting of the init coordinates
        tileCount = 1
        xMax = xMin = sumX = x
        yMax = yMin = sumY = y
        crtPos = 1          #crt position in the queue
        queue = [(x, y)]
        self.__table.setValue(x, y, TEMP_SYMBOL)
        
        while crtPos <= len(queue):
            for direction in range(8):
                newX = x + X_DIR[direction]
                newY = y + Y_DIR[direction]
                
                if 0 <= newX < self.__table.height and 0 <= newY < self.__table.width and self.__table.getValue(newX, newY) == EMPTY_SYMBOL:
                    queue.append((newX, newY))
                    self.__table.setValue(newX, newY, TEMP_SYMBOL)
                    
                    if xMax < newX:
                        xMax = newX
                    if xMin > newX:
                        xMin = newX
                    if yMax < newY:
                        yMax = newY
                    if yMin > newY:
                        yMin = newY
                        
                    tileCount += 1
                    sumX += newX
                    sumY += newY
            crtPos += 1
            
        #restore the table
        for pos in range(len(queue)):
            self.__table.setValue(queue[pos][0], queue[pos][1], EMPTY_SYMBOL)
            
        return (tileCount, xMax, yMax, xMin, yMin, sumX, sumY)
    
    def __round(self, value, count):
        '''
        Rounds an arithmetic mean to the closest integer
        @param:
            - value = integer, sum of elements
            - count = integer, nr of elements
        @return:
            - integer value, the closest integer to the mean
        @raise:
            - None
        '''
        result = value / count
        frac = result - int(result)
        
        if frac <= 0.5:
            return int(result)
        return int(result) + 1
     
    def __moveToWin(self):
        '''
        Determines the coordinates for a winning move, if possible
        @param:
            - None
        @return:
            - (xCoord, yCoord) = integers, the coordinates where the move needs to be made, if it is possible
            - None, otherwise
        @raise:
            - None
        '''
        if self.__table.emptyCells > 9:
            return None
        
        for x in range(self.__table.height):
            for y in range(self.__table.width):
                if self.__table.getValue(x, y) == EMPTY_SYMBOL:
                    (tileCount, xMax, yMax, xMin, yMin, sumX, sumY) = self.__processEmptyArea(x, y)
                    if tileCount == self.__table.emptyCells and xMax - xMin < 3 and yMax - yMin < 3:
                        return (self.__round(sumX, tileCount), self.__round(sumY, tileCount))
        
    def computerMove(self):
        '''
        Performs a computer move
        @param:
            - None
        @return:
            - PLAYER_SYMBOL = character, if the player has won
            - COMPUTER_SYMBOL = character, if the computer has won
            - None, if the game is not over
        @raise:
            - None
        '''
        #the computer cannot move, thus the player has won
        if self.__table.isFull() == True:
            return PLAYER_SYMBOL
        
        #version 1, first empty position
        #(xCoord, yCoord) = self.__table.getFirstEmpty()
        
        #version 1.1, random position
        #coordList = self.__table.getAllEmpty()
        #(xCoord, yCoord) = random.choice(coordList)
        
        #version 2, random position, but the computer will move to win if possible
        result = self.__moveToWin()
        if result != None:
            (xCoord, yCoord) = result
        else:
            coordList = self.__table.getAllEmpty()
            (xCoord, yCoord) = random.choice(coordList)
        
        self.__move(xCoord, yCoord, COMPUTER_SYMBOL)
        
        #the player cannot move, thus the computer has won
        if self.__table.isFull() == True:
            return COMPUTER_SYMBOL
    
    def toPrint(self):
        return self.__table.content()
    
    def getTable(self):
        return self.__table
        
    