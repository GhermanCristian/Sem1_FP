from texttable import Texttable
from gameEngine import GameEngine
from constants import PLAYER_SYMBOL, COMPUTER_SYMBOL

class NormalUI(object):
    def __init__(self):
        pass
    
    def __getPlayerChoice(self):
        '''
        Gets user input regarding the order of playing
        @param:
            - None
        @return:
            - playerChoice = integer, valid
        @raise:
            - TypeError, if the input values are not integers
            - ValueError, if the playerChoice is out of range
        '''
        while True:
            playerChoice = input("Player 1, player 2 or random (0)?\n")
            
            try:
                playerChoice = int(playerChoice)
                if playerChoice not in [0, 1, 2]:
                    raise ValueError("Invalid player")
                return playerChoice
            
            except Exception as e:
                print (str(e))
    
    def __getBoardSize(self):
        '''
        Gets user input regarding the table size
        @param:
            - None
        @return:
            - tuple of the form (boardWidth, boardHeight) (both valid integers)
        @raise:
            - TypeError, if the input values are not integers
            - ValueError, if the table size is invalid
        '''
        while True:
            boardWidth = input("Please insert the board width: ")
            boardHeight = input("Please insert the board height: ")
            
            try:
                boardWidth = int(boardWidth)
                boardHeight = int(boardHeight)
                if boardWidth <= 0 or boardHeight <= 0:
                    raise ValueError("Invalid table size")
                return (boardWidth, boardHeight)
            
            except Exception as e:
                print (str(e))
    
    def __printTable(self, boardHeight, boardWidth, board):
        '''
        Prints the table using the textTable module
        @param:
            - boardHeight, boardWidth - integers, the size of the table
            - board = entity of type Table
        @return:
            - None
        @raise:
            - None
        '''
        t = Texttable()

        #add a header row with the box coordinates
        header = [" "]
        header.extend(list(range(0, boardWidth)))
        header.append(" ")
        t.add_row(header)
        
        for i in range(boardHeight):
            #add a header column with the box coordinates
            aux = [i]
            
            aux.extend(board[i])
            aux.append(i)
            t.add_row(aux)
        
        #copy the header row as a footer
        t.add_row(header)
        print (t.draw())
    
    def __getPlayerCoords(self):
        '''
        Gets the coordinates on which to move, given by the user
        @param:
            - None
        @return:
            - a tuple which contains the coordinates of the move
        @raise:
            - TypeError, if the input values are not integers
        '''
        while True:
            xCoord = input("Please insert xCoord: ")
            yCoord = input("Please insert yCoord: ")
            
            try:
                xCoord = int(xCoord)
                yCoord = int(yCoord)
                return (xCoord, yCoord)
            
            except Exception as e:
                print (str(e)) 
                
    def __printResult(self, result):
        if result == PLAYER_SYMBOL:
            print ("You've won")
             
        if result == COMPUTER_SYMBOL:
            print ("You've lost")
    
    def start(self):
        #choose player
        playerChoice = self.__getPlayerChoice()
            
        #choose table size
        (boardWidth, boardHeight) = self.__getBoardSize()
            
        gameEngine = GameEngine(playerChoice, boardWidth, boardHeight)    
        #self.__printTable(boardHeight, boardWidth, [[" "] * boardWidth] * boardHeight)
            
        while True:
            #the player moves first
            if playerChoice == 1:
                (xCoord, yCoord) = self.__getPlayerCoords()
                try:
                    result = gameEngine.playerMove(xCoord, yCoord)
                    if result != None:
                        self.__printResult(result)
                        return
                except Exception as e:
                    print (str(e))
                    continue
                
                self.__printTable(boardHeight, boardWidth, gameEngine.toPrint())
                
                result = gameEngine.computerMove()
                if result != None:
                    self.__printResult(result)
                    return
            
            #the computer moves first
            elif playerChoice == 2:
                result = gameEngine.computerMove()
                if result != None:
                    self.__printResult(result)
                    return
                
                self.__printTable(boardHeight, boardWidth, gameEngine.toPrint())
                
                (xCoord, yCoord) = self.__getPlayerCoords()
                try:
                    result = gameEngine.playerMove(xCoord, yCoord)
                    if result != None:
                        self.__printResult(result)
                        return
                except Exception as e:
                    print (str(e))
                    continue

            self.__printTable(boardHeight, boardWidth, gameEngine.toPrint())
            
            
            




