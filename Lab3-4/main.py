'''
Assignment 3-4: due on 22/29 Oct 2019
Problem 2 ("Contest")
'''

from constants import COMMAND_ID
from modifyCommands import add, insert, remove, replace, undo
from UICommands import listStudents, average, minimumScore, topStudent
from UIFunctions import getUIChoice
from exampleLists import exampleList1, exampleList2, exampleList3, exampleList10

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
        add, 
        insert, 
        remove, 
        replace, 
        listStudents, 
        average, 
        minimumScore, 
        topStudent,
        undo
    ]

    #the first 4 commands actually modify the studentList
    #in this function, commandID will never be 0
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
            newStudentList = undo(studentList, commandParams, commandStack)
            if newStudentList != -1:
                studentList = newStudentList[:]
                
        else:
            executeCommand(commandID, commandParams, studentList, commandStack)

if __name__ == "__main__":
    main()
    
    