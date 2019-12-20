from texttable import Texttable
from gameEngine import GameEngine
from constants import PLAYER_SYMBOL, COMPUTER_SYMBOL

class NormalUI(object):
    def __init__(self):
        pass
    
    def __getPlayerChoice(self):
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
        while True:
            boardWidth = input("Please insert the board width: ")
            boardHeight = input("Please insert the board height: ")
            
            try:
                boardWidth = int(boardWidth)
                boardHeight = int(boardHeight)
                if boardHeight * boardWidth <= 0 or boardHeight < 0:
                    raise ValueError("Invalid table size")
                return (boardWidth, boardHeight)
            
            except Exception as e:
                print (str(e))
    
    def __printTable(self, boardHeight, boardWidth, board):
        t = Texttable()

        header = [" "]
        header.extend(list(range(0, boardWidth)))
        header.append(" ")
        t.add_row(header)
        
        for i in range(boardHeight):
            aux = [i]
            aux.extend(board[i])
            aux.append(i)
            t.add_row(aux)
        
        t.add_row(header)
        print (t.draw())
    
    def __getPlayerCoords(self):
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
            #player moves first
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
            
            #computer moves first
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
            
            
            




