import pygame
from pygame.locals import *
from constants import *
from pygame.constants import *
from transition import Transition

class GUI(object):
    '''
    Class for the 
    Fields:
        Public:
            - None
        Private:
            - None
    Methods:
        Public:
            - None
        Private:
            - None
    Properties:
        - None
    Setters:
        - None
    '''
    def __init__(self):
        pygame.init()
        self.__appDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption(APP_TITLE)
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.SysFont(GAME_FONT, GAME_FONT_SIZE, True, False)
        
        self.__mouseX = 0
        self.__mouseY = 0
        self.__mouseClicked = False
        
        self.__trans = Transition()
        self.__commandName = [
            ["Add client", "- client name"],
            ["Remove client", "- client ID"],
            ["Update client", "- ID", '''- "name"''', "- new name"],
            ["Add movie", "- movie title", "- movie desc", "- movie genre"],
            ["Remove movie", "- movie ID"],
            ["Update movie"],
            ["Print list", '''- "client"''', '''- "movie"'''],
            ["Rent movie", "- clientID", "- movieID", "- rentDate", "- returnDate"],
            ["Return movie", "- clientID", "- movieID"],
            ["Search client", "- ID", "- name"],
            ["Search movie", "- ID", "- title", "- description", "- genre"],
            ["Most active", '''- "client"''', '''- "movie"'''],
            ["Late rentals"],
            ["Undo"],
            ["Redo"]
        ]
        
        self.__page = 0
    
    def __displayText(self, text, xPos, yPos, font, color):
        '''
        
        @param:
            -
        @return:
            -
        '''
        self.__appDisplay.blit(self.__font.render(text, True, color, None), (xPos, yPos))
    
    def __drawBox(self, left, top, isScroll = 0):
        '''
        
        @param:
            -
        @return:
            -
        '''
        pygame.draw.rect(self.__appDisplay, BOX_COLOR, (left, top, BOX_WIDTH, BOX_HEIGHT))
        if isScroll == 1:
            self.__displayText("Previous page", left + 20, top + 20, self.__font, TEXT_COLOR)
        elif isScroll == 2:
            self.__displayText("Next page", left + 20, top + 20, self.__font, TEXT_COLOR)
    
    def __drawBoxes(self):
        '''
        
        @param:
            -
        @return:
            -
        '''
        for i in range(5):
            for j in range(3):
                xPos = LATERAL_MARGIN + j * (BOX_WIDTH + GAP_SIZE)
                yPos = UPPER_MARGIN + i * (BOX_HEIGHT + GAP_SIZE)
                self.__drawBox(xPos, yPos)
                for k in range(len(self.__commandName[i * 3 + j])):
                    self.__displayText(self.__commandName[i * 3 + j][k], xPos + 20, yPos + 10 + k * GAME_FONT_SIZE, self.__font, TEXT_COLOR)
    
    def __drawPanel(self, left, top):
        '''
        
        @param:
            -
        @return:
            -
        '''
        pygame.draw.rect(self.__appDisplay, PANEL_COLOR, (left, top, PANEL_WIDTH, PANEL_HEIGHT))
    
    def __drawBar(self, left, top, color):
        '''
        
        @param:
            -
        @return:
            -
        '''
        pygame.draw.rect(self.__appDisplay, color, (left, top, BAR_WIDTH, BAR_HEIGHT))
    
    def __getBoxAtPixel(self, x, y):
        '''
        
        @param:
            -
        @return:
            -
        '''
        # search in the command boxes
        for i in range(5):
            for j in range(3):
                left = LATERAL_MARGIN + j * (BOX_WIDTH + GAP_SIZE)
                top = UPPER_MARGIN + i * (BOX_HEIGHT + GAP_SIZE)
                boxRect = pygame.Rect(left, top, BOX_WIDTH, BOX_HEIGHT)
                if boxRect.collidepoint(x, y):
                    return (i, j)
                
        # search in the scroll boxes
        left = WINDOW_WIDTH - LATERAL_MARGIN - PANEL_WIDTH / 2 - BOX_WIDTH - 25
        top = UPPER_MARGIN + PANEL_HEIGHT + GAP_SIZE
        box1 = pygame.Rect(left, top, BOX_WIDTH, BOX_HEIGHT)
        if box1.collidepoint(x, y):
            return 1
        
        left = WINDOW_WIDTH - LATERAL_MARGIN - PANEL_WIDTH / 2 + 25
        top = UPPER_MARGIN + PANEL_HEIGHT + GAP_SIZE
        box2 = pygame.Rect(left, top, BOX_WIDTH, BOX_HEIGHT)
        if box2.collidepoint(x, y):
            return 2
        
        return None
    
    def __getUserInput(self):
        '''
        
        @param:
            -
        @return:
            -
        '''
        userInput = ""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    quit()
                    return None
                if event.type == KEYDOWN:
                    if event.unicode.isalnum() or event.unicode in "!@#$%^&*()_+-=<>,.?/:{}\|`~ ":
                        userInput += event.unicode
                    elif event.key == K_BACKSPACE:
                        userInput = userInput[:-1]
                    elif event.key == K_RETURN:
                        return userInput[:MAX_STRING_LEN]
            
            self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN, LIGHT_BAR_COLOR)
            self.__displayText(userInput, LATERAL_MARGIN + 20, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN + 12, self.__font, TEXT_COLOR)
            pygame.display.update() 
           
    def __printToPanel(self, entityList, printType):
        '''
        
        @param:
            -
        @return:
            -
        '''
        i = 0
        left = 3 * LATERAL_MARGIN + 3 * BOX_WIDTH + 2 * GAP_SIZE + 25
        
        #repository
        if not isinstance(entityList, list):
            IDList = []
            for entity in entityList:
                IDList.append(entity.ID)
            IDList.sort()
        
            for ID in IDList[self.__page * ITEMS_PER_PAGE : (self.__page + 1) * ITEMS_PER_PAGE]:
                toPrint = str(entityList[ID]).split('\n') 
                for j in toPrint:
                    self.__displayText(j, left, UPPER_MARGIN + i * GAME_FONT_SIZE + 5, self.__font, TEXT_COLOR)
                    i += 1
        
        else:
            for entity in entityList[self.__page * ITEMS_PER_PAGE : (self.__page + 1) * ITEMS_PER_PAGE]:
                if printType == "normalList":
                    toPrint = str(entity).split('\n') 
                elif printType == "daysList":
                    toPrint = ("Days rented: " + str(entity.daysRented) + "\n" + str(entity)).split('\n') 
                elif printType == "lateList":
                    toPrint = ("Days late: " + str(entity.daysLate()) + "\n" + str(entity)).split('\n')
                for j in toPrint:
                    self.__displayText(j, left, UPPER_MARGIN + i * GAME_FONT_SIZE + 5, self.__font, TEXT_COLOR)
                    i += 1

    def __printError(self, text):
        '''
        
        @param:
            -
        @return:
            -
        '''
        self.__displayText(text, LATERAL_MARGIN + 25, WINDOW_HEIGHT - LOWER_MARGIN - BAR_HEIGHT + 12, self.__font, TEXT_COLOR)
        pygame.display.update()
        
    def __turnPage(self, val, nrOfItems):
        '''
        
        @param:
            -
        @return:
            -
        '''
        if val == 1:
            if self.__page > 0:
                self.__page -= 1
        else:
            if self.__page + 1 < nrOfItems / ITEMS_PER_PAGE:
                self.__page += 1
            
    def __initAppDisplay(self):
        '''
        
        @param:
            -
        @return:
            -
        '''
        self.__appDisplay.fill(BG_COLOR)
        
        #command boxes
        self.__drawBoxes()
        
        #info panel
        self.__drawPanel(3 * LATERAL_MARGIN + 3 * BOX_WIDTH + 2 * GAP_SIZE, UPPER_MARGIN)
        
        #user input bar
        self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN, BAR_COLOR)
        
        #error bar
        self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - BAR_HEIGHT, BAR_COLOR)
        
        #left scroll box
        self.__drawBox(WINDOW_WIDTH - LATERAL_MARGIN - PANEL_WIDTH / 2 - BOX_WIDTH - 25, UPPER_MARGIN + PANEL_HEIGHT + GAP_SIZE, 1)
        
        #right scroll box
        self.__drawBox(WINDOW_WIDTH - LATERAL_MARGIN - PANEL_WIDTH / 2 + 25, UPPER_MARGIN + PANEL_HEIGHT + GAP_SIZE, 2)         
            
    def start(self):
        '''
        
        @param:
            -
        @return:
            -
        '''
        canPrintError = False
        canPrintPanel = False
        
        callResult = None
        
        while True:
            self.__initAppDisplay()
            
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    quit()
                elif event.type == MOUSEMOTION:
                    self.__mouseX, self.__mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    self.__mouseX, self.__mouseY = event.pos
                    self.__mouseClicked = True
            
            if self.__mouseClicked == True:
                self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN, BAR_COLOR)
                self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - BAR_HEIGHT, BAR_COLOR)
           
                self.__mouseClicked = False
                result = self.__getBoxAtPixel(self.__mouseX, self.__mouseY)
                
                if result is not None:
                    try:
                        xCoord = result[0]
                        yCoord = result[1]
                        
                        #if we have clicked on a command, stop printing errors or info to the panel
                        canPrintError = False
                        canPrintPanel = False
                        self.__page = 0
                        
                        commandID = xCoord * 3 + yCoord + 1
                        #these functions don't require any other input, hence I can skip the getInput part
                        if commandID in [13, 14, 15]:
                            userInput = []
                        else:
                            userInput = self.__getUserInput().split()
                        
                        callResult = self.__trans.call(commandID, userInput)
                        #the part below only concers printing, so in this case I can skip it
                        if callResult == None:
                            continue
                        
                        if len(callResult) == 0:
                            callResult = ["Empty"]
                        
                        #mostActive
                        if commandID == 12:
                            printType = "daysList"
                        #lateRentals
                        elif commandID == 13:
                            printType = "lateList"
                        #searchClient, searchMovie
                        else:
                            printType = "normalList"
                    
                        #print either an error, or to the panel, according to the result of the command
                        if isinstance(callResult, str):
                            canPrintError = True
                        elif callResult != None:
                            canPrintPanel = True
                        
                    except:
                        if callResult == None:
                            continue
                        scrollBox = result
                        self.__turnPage(scrollBox, len(callResult))
            
            #print error message to the error Bar
            if canPrintError == True:
                self.__printError(callResult)   
                
            #print information to the panel
            if canPrintPanel == True:
                self.__printToPanel(callResult, printType)
                
            pygame.display.update()
            self.__clock.tick(FPS)


