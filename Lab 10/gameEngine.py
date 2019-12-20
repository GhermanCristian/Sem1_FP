import random
from table import Table
from customExceptions import EmptyError
from constants import *

class GameEngine(object):
    def __init__(self, player, boardWidth, boardHeight):
        if player == 0:
            self.__player = random.randint(1,2)
        else:
            self.__player = player
            
        self.__table = Table(boardWidth, boardHeight)
        
    def __move(self, xCoord, yCoord, value):
        if self.__table.getValue(xCoord, yCoord) != EMPTY_SYMBOL:
            raise EmptyError("Position is not empty")
        
        for i in range(xCoord - 1, xCoord + 2):
            for j in range(yCoord - 1, yCoord + 2):
                self.__table.setValue(i, j, OCCUPIED_SYMBOL)    
        
        self.__table.setValue(xCoord, yCoord, value)   
        
    def playerMove(self, xCoord, yCoord):
        if self.__table.isFull() == True:
            return COMPUTER_SYMBOL
        
        self.__move(xCoord, yCoord, PLAYER_SYMBOL)
        
    def computerMove(self):
        if self.__table.isFull() == True:
            return PLAYER_SYMBOL
        
        #version 1, first empty position
        #(xCoord, yCoord) = self.__table.getFirstEmpty()
        
        #version 1.1, random position
        coordList = self.__table.getAllEmpty()
        (xCoord, yCoord) = random.choice(coordList)
        
        self.__move(xCoord, yCoord, COMPUTER_SYMBOL)
        
    def toPrint(self):
        return self.__table.getPrintable()
        
    