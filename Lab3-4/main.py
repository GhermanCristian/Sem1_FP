'''
Assignment 3-4: due on 22/29 Oct 2019
Problem 2 ("Contest")

Module description:
    - constants = contains constant values, to be used by all modules
    - customExceptions = contains user-defined errors
    - exampleList = contains hard-coded, valid lists
    - interact = setters and getters
    - main = main module (UI) and the one which is called to run the program
    - nonUIFunctions = functions which are not UI and which are used by other modules
    - nonUIImplementation = the implementation of non-UI domain functions (add, insert, remove, replace, undo)
    - regexPatterns = contains regex patterns to be used by either the command-UI or menu-UI
    - testing = contains test functions
    - UICommands = the UI domain functions (list, average, minimum, top)
    - UIFunctions = functions which are UI and which are used by other modules
    - UIModifyCommands = the interface of the functions which modify the list (add, insert, remove, replace, undo)
    - validators = functions which validate various input values and which raise exceptions
    
 The user first chooses the type of UI - this will return a regex pattern list, which will be used from there on.
 Each command inputted by the user is checked against the regex pattern list, and then, if valid, will return a
commandID and a list of parameters. (each command has a commandID, to ease the implementation of both menu-UI and
command-UI)
 Every action has an UI interface, in which the input is parsed.
'''

# interface of the commands which modify the list
from UIModifyCommands import addUI, insertUI, removeUI, replaceUI, undoUI
# interface of the commands which are strictly UI (don't modify the list)
from UICommands import listStudents, average, minimumScore, topStudent
# functions used to get user input
from UIFunctions import getUIChoice, getAction
from exampleLists import exampleList1, exampleList10
from regexPatterns import COM_patternList, MEN_patternList, UI_TYPE_PATTERN

def executeCommand(commandID, paramList, studentList, commandStack):
    '''
    Executes a command based on its ID and parameters
    @param:
        - commandID = integer representing the ID of a particular command
        - paramList = list of parameters which can be used by the commands
        - studentList = list of students
        - commandStack = list, organized as a stack, with which we can perform undo operations
    @return:
        - None
    '''
    COMMAND_LIST = [
        exit,
        addUI, 
        insertUI, 
        removeUI, 
        replaceUI, 
        listStudents, 
        average, 
        minimumScore, 
        topStudent,
        undoUI
    ]

    # the first 4 commands actually modify the studentList,
    # so I need to make a copy of current state of the list
    if commandID <= 4:
        commandStack.append(studentList[:])
        
    COMMAND_LIST[commandID](studentList, paramList)

def main():
    studentList = exampleList1
    commandStack = []
    
    #prompt user for the desired UI
    patternList = getUIChoice(UI_TYPE_PATTERN, COM_patternList, MEN_patternList)
    
    while True:
        commandID, paramList = getAction(patternList)
        
        #exit command
        if commandID == 0:
            print ("Program has ended")
            return 
        
        #undo
        elif commandID == 9:
            undoUI(studentList, commandStack)
                
        else:
            executeCommand(commandID, paramList, studentList, commandStack)

if __name__ == "__main__":
    main()
    
    