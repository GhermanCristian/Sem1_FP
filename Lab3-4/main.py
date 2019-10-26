'''
Assignment 3-4: due on 22/29 Oct 2019
Problem 2 ("Contest")
'''

from constants import COMMAND_ID
from UIModifyCommands import addUI, insertUI, removeUI, replaceUI, undoUI
from UICommands import listStudents, average, minimumScore, topStudent
from UIFunctions import getUIChoice
from exampleLists import exampleList1, exampleList10

def executeCommand(commandID, commandParams, studentList, commandStack):
    '''
    Executes a command based on its ID and parameters
    @param:
        - commandID = integer representing the ID of a particular command
        - commandParams = list of parameters which can be used by the commands
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
        
    COMMAND_LIST[commandID](studentList, commandParams)

def main():
    studentList = exampleList10
    commandStack = []
    
    #prompt user for the desired UI
    UIType = getUIChoice()
    
    while True:
        commandID, commandParams = UIType(COMMAND_ID)
        
        #exit command
        if commandID == 0:
            print ("Program has ended")
            return 
        
        #undo
        elif commandID == 9:
            undoUI(studentList, commandParams, commandStack)
                
        else:
            executeCommand(commandID, commandParams, studentList, commandStack)

if __name__ == "__main__":
    main()
    
    