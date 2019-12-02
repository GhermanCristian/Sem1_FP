import pygame
from pygame.locals import *
from constants import *
from pygame.constants import *
from transition import Transition

class GUI(object):
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
            "Add client",
            "Remove client",
            "Update client",
            "Add movie",
            "Remove movie",
            "Update movie",
            "Print list",
            "Rent movie",
            "Return movie",
            "Search client",
            "Search movie",
            "Most active",
            "Late rentals",
            "Undo",
            "Redo"
        ]
        
        self.__page = 0
    
    def __displayText(self, text, xPos, yPos, font, color):
        self.__appDisplay.blit(self.__font.render(text, True, color, None), (xPos, yPos))
    
    def __drawBox(self, left, top):
        pygame.draw.rect(self.__appDisplay, BOX_COLOR, (left, top, BOX_WIDTH, BOX_HEIGHT))
    
    def __drawBoxes(self):
        for i in range(5):
            for j in range(3):
                xPos = LATERAL_MARGIN + j * (BOX_WIDTH + GAP_SIZE)
                yPos = UPPER_MARGIN + i * (BOX_HEIGHT + GAP_SIZE)
                self.__drawBox(xPos, yPos)
                self.__displayText(self.__commandName[i * 3 + j], xPos, yPos, self.__font, TEXT_COLOR)
    
    def __drawPanel(self, left, top):
        pygame.draw.rect(self.__appDisplay, BAR_COLOR, (left, top, PANEL_WIDTH, PANEL_HEIGHT))
    
    def __drawBar(self, left, top):
        pygame.draw.rect(self.__appDisplay, BAR_COLOR, (left, top, BAR_WIDTH, BAR_HEIGHT))
    
    def __getBoxAtPixel(self, x, y):
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
                        return userInput[:80]
            
            self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN)
            self.__displayText(userInput, LATERAL_MARGIN + 5, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN + 5, self.__font, TEXT_COLOR)
            pygame.display.update() 
           
    def __printToPanel(self, entityList):
        i = 0
        left = 3 * LATERAL_MARGIN + 3 * BOX_WIDTH + 2 * GAP_SIZE + 5
        
        self.__trans.setIgnoreFlag(True)
        
        for entity in entityList[self.__page * ITEMS_PER_PAGE : (self.__page + 1) * ITEMS_PER_PAGE]:
            printList = str(entity).split('\n') 
            for j in printList:
                self.__displayText(j, left, UPPER_MARGIN + i * GAME_FONT_SIZE, self.__font, TEXT_COLOR)
                i += 1
            
        self.__trans.setIgnoreFlag(False)

    def __printError(self, text):
        self.__displayText(text, LATERAL_MARGIN + 5, WINDOW_HEIGHT - LOWER_MARGIN - BAR_HEIGHT + 5, self.__font, TEXT_COLOR)
        pygame.display.update()
        
    def __turnPage(self, val):
        if val == 1:
            if self.__page > 0:
                self.__page -= 1
        else:
            if self.__page < 3:
                self.__page += 1
            
    def start(self):
        canPrintError = False
        canPrintPanel = False
        
        while True:
            self.__appDisplay.fill(BG_COLOR)
            self.__drawBoxes()
            self.__drawPanel(3 * LATERAL_MARGIN + 3 * BOX_WIDTH + 2 * GAP_SIZE, UPPER_MARGIN)
            self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN)
            self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - BAR_HEIGHT)
            self.__drawBox(WINDOW_WIDTH - LATERAL_MARGIN - PANEL_WIDTH / 2 - BOX_WIDTH - 25, UPPER_MARGIN + PANEL_HEIGHT + GAP_SIZE)
            self.__drawBox(WINDOW_WIDTH - LATERAL_MARGIN - PANEL_WIDTH / 2 + 25, UPPER_MARGIN + PANEL_HEIGHT + GAP_SIZE)
            
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    quit()
                elif event.type == MOUSEMOTION:
                    self.__mouseX, self.__mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    self.__mouseX, self.__mouseY = event.pos
                    self.__mouseClicked = True
            
            if self.__mouseClicked == True:
                # kind of a re-initialisation
                self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - 2 * BAR_HEIGHT - UPPER_MARGIN)
                self.__drawBar(LATERAL_MARGIN, WINDOW_HEIGHT - LOWER_MARGIN - BAR_HEIGHT)
           
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
                        #these functions don't require any other input
                        if commandID in [13, 14, 15]:
                            userInput = []
                        else:
                            userInput = self.__getUserInput().split()
                        
                        callResult = self.__trans.call(commandID, userInput)
                    
                        #print according to the result of the command
                        if isinstance(callResult, str):
                            canPrintError = True
                        elif callResult != None:
                            canPrintPanel = True
                        
                    except:
                        scrollBox = result
                        self.__turnPage(scrollBox)
                
            if canPrintError == True:
                self.__printError(callResult)   
                
            if canPrintPanel == True:
                self.__printToPanel(callResult)
                
            pygame.display.update()
            self.__clock.tick(FPS)


