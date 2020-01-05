import pygame
from pygame.constants import *
from constants import *
from gameEngine import GameEngine

class GUI(object):
    def __init__(self):
        pygame.init()
        self.__gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption(APP_TITLE)
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.SysFont(GAME_FONT, GAME_FONT_SIZE, True, False)
        
        self.__mouseX = 0
        self.__mouseY = 0
        self.__mouseClicked = False
        
        self.__moveMade = False
        
    def __leftTopCoords(self, i, j, tableWidth, tableHeight):
        leftCorner = Y_CENTER - (tableWidth // 2  * (BOX_SIZE + GAP_SIZE))
        topCorner = X_CENTER - (tableHeight // 2  * (BOX_SIZE + GAP_SIZE))
        
        left = leftCorner + j * (BOX_SIZE + GAP_SIZE)
        top = topCorner + i * (BOX_SIZE + GAP_SIZE)
        
        return left, top
        
    def __getBoxAtPixel(self, tableWidth, tableHeight, x, y):
        '''
        Determines the box at a given pixel
        @param:
            - tableWidth, tableHeight - integers, the size of the table
            - x, y - integers, the coordinates of the pixel
        @return:
            - a tuple containing the box's coordinates inside the table, if the pixel is inside a box
            - a tuple of None elements, otherwise
        '''
        for i in range(tableHeight):
            for j in range(tableWidth):
                left, top = self.__leftTopCoords(i, j, tableWidth, tableHeight)
                boxRect = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
                if boxRect.collidepoint(x, y):
                    return (i, j)
                
        return (None, None)
    
    def __drawHighlight(self, tableWidth, tableHeight, i, j):
        '''
        Highlights a box when the mouse cursor is over it
        '''
        self.__drawBox(tableWidth, tableHeight, i, j, MOUSEOVER_TILE)
        
    def __drawBox(self, tableWidth, tableHeight, i, j, boxColor):
        '''
        Draws a box on a given position and with a given color
        @param:
            - tableWidth, tableHeight - integers, the size of the table
            - i, j - integers, the position of the box in the table
            - boxColor - tuple (RGB), the color of the box
        @return:
            - None
        @raise:
            - None
        '''
        left, top = self.__leftTopCoords(i, j, tableWidth, tableHeight)
        pygame.draw.rect(self.__gameDisplay, boxColor, (left, top, BOX_SIZE, BOX_SIZE))
        
    def __drawTable(self, table):
        '''
        Draws the entire table, box by box
        @param:
            - table = entity of type Table
        @return:
            - None
        @raise:
            - None
        '''
        #associates each symbol to a color
        colorDict = {
            PLAYER_SYMBOL: PLAYER_TILE,
            COMPUTER_SYMBOL: COMPUTER_TILE,
            OCCUPIED_SYMBOL: OCCUPIED_TILE,
            EMPTY_SYMBOL: EMPTY_TILE
        }
        
        for i in range(table.height):
            for j in range(table.width): 
                self.__drawBox(table.width, table.height, i, j, colorDict[table.getValue(i, j)])
    
    def __displayText(self, text, xPos, yPos, font, color):
        '''
        Displays a text at a given position, with a font and a color
        @param:
            - xPos, yPos - integers, the left/ top coordinates of the 'text box'
            - font - of type pygame.font
            - color - tuple (RGB)
        @return:
            - None
        @raise:
            - None
        '''
        self.__gameDisplay.blit(font.render(text, True, color, None), (xPos, yPos))
    
    def __getUserInput(self, promptText):
        '''
        Receives user input
        @param:
            - promptText = string; message which is displayed to the user
        @return:
            - userInput = string; the message given by the user
        '''
        userInput = ""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    quit()
                    return None
                if event.type == KEYDOWN:
                    #the input will only contain digits, so we do not concern with other characters
                    if event.unicode.isnumeric():
                        userInput += event.unicode
                    elif event.key == K_BACKSPACE:
                        #delete the last character
                        userInput = userInput[:-1]
                    elif event.key == K_RETURN:
                        return userInput[:]
            
            leftCorner = Y_CENTER - 50
            topCorner = X_CENTER - 50
            
            self.__gameDisplay.fill(BG_COLOR)
            self.__displayText(promptText, leftCorner - 300, topCorner - 100, self.__font, TEXT_COLOR)
            #the text is displayed as it is written
            self.__displayText(userInput, leftCorner, topCorner, self.__font, TEXT_COLOR)
            pygame.display.update()
      
    def __endRound(self, result, table):
        '''
        Verifies the posibility of the round having ended and acts accordingly
        @param:
            - result = character -> None, COMPUTER_SYMBOL or PLAYER_SYMBOL
            - table = entity of type Table
        @return:
            - None
        @raise:
            - None
        '''
        if result == None:
            return
    
        self.__drawTable(table)
        pygame.display.update()
        pygame.time.wait(500)
    
        self.__gameDisplay.fill(BG_COLOR)
    
        if result == COMPUTER_SYMBOL:
            self.__displayText("You've lost", Y_CENTER - 100, X_CENTER - 50, self.__font, TEXT_COLOR)
        
        else:
            self.__displayText("You've won", Y_CENTER - 100, X_CENTER - 50, self.__font, TEXT_COLOR)
            
        pygame.display.update()
        pygame.time.wait(1000)
        quit()
        
    def __getPlayer(self):
        '''
        Gets user input regarding the order of playing
        @param:
            - None
        @return:
            - playerChoice = integer, valid
        @raise:
            - None
        '''
        while True:
            playerChoice = int(self.__getUserInput("Player 1, player 2 or random (0)?"))
            
            if playerChoice in [0, 1, 2]:
                return playerChoice  
        
    def __getTableSize(self):
        '''
        Gets user input regarding the table size
        @param:
            - None
        @return:
            - tuple of the form (boardWidth, boardHeight) (both valid integers)
        @raise:
            - None
        '''
        while True:
            boardWidth = int(self.__getUserInput("Please insert the board width: "))
            boardHeight = int(self.__getUserInput("Please insert the board height: "))
            
            if boardWidth > 0 and boardHeight > 0:
                return (boardWidth, boardHeight)
    
    def __play(self, player, gameEngine):
        self.__gameDisplay.fill(BG_COLOR)
            
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                quit()
            elif event.type == MOUSEMOTION:
                self.__mouseX, self.__mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.__mouseX, self.__mouseY = event.pos
                self.__mouseClicked = True
               
        table = gameEngine.getTable()
        self.__drawTable(table)
        boxX, boxY = self.__getBoxAtPixel(table.width, table.height, self.__mouseX, self.__mouseY)
        
        #the player moves first, then the computer
        if player == 1:
            if boxX != None and boxY != None:
                self.__drawHighlight(table.width, table.height, boxX, boxY)
                if self.__mouseClicked == True:
                    self.__mouseClicked = False
                    if table.getValue(boxX, boxY) == EMPTY_SYMBOL:
                        result = gameEngine.playerMove(boxX, boxY)
                        self.__endRound(result, table)
                        result = gameEngine.computerMove()
                        self.__endRound(result, table)

        #the computer moves first, then the player
        else:
            if self.__moveMade == False:
                result = gameEngine.computerMove()
                self.__endRound(result, table)
                self.__moveMade = True
                
            if boxX != None and boxY != None:
                self.__drawHighlight(table.width, table.height, boxX, boxY)
                if self.__mouseClicked == True:
                    self.__mouseClicked = False
                    if table.getValue(boxX, boxY) == EMPTY_SYMBOL:
                        result = gameEngine.playerMove(boxX, boxY)
                        self.__endRound(result, table)
                        self.__moveMade = False
        
        pygame.display.update()
        self.__clock.tick(FPS)
        
    def start(self):
        player = self.__getPlayer()
        (tableWidth, tableHeight) = self.__getTableSize()
        gameEngine = GameEngine(player, tableWidth, tableHeight)
        
        while True:
            self.__play(player, gameEngine)


