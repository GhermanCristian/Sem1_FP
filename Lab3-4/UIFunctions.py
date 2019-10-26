from validators import getValidNumber
from interact import *
from constants import UI_PROMPT_TEXT, MENU_UI_TEXT
from customExceptions import ParamError

def menuBasedUI(COMMAND_ID):
    '''
    (menu-based version)
    Determines the command and parameter list inputted by the user
    @param:
        - COMMAND_ID = dictionary which pairs all the commands with an ID
    @return:
        -a tuple of the form (commandID, paramList)
    '''
    while True:
        inputCommand = input("Please insert the command and the arguments: ")
        
        if len(inputCommand) > 0:
            inputCommand.strip()
            inputCommand = inputCommand.split()
            
            commandID = getValidNumber(inputCommand[0], 'I', 0, 9)
            if commandID != -1:
                return (commandID, inputCommand[1:])
        
        print ("Invalid command")

def commandBasedUI(COMMAND_ID):
    '''
    (command-based version)
    Determines the command and parameter list inputted by the user
    @param:
        - COMMAND_ID = dictionary which pairs all the commands with an ID
    @return:
        -a tuple of the form (commandID, paramList)
    '''
    while True:
        inputCommand = input("Please insert the command and the arguments: ")
        
        try:
            if len(inputCommand) == 0:
                raise ParamError("Invalid command")
        
        except:
            pass
        
        inputCommand.strip()
        inputCommand = inputCommand.split()
        inputCommand[0] = inputCommand[0].lower()
            
        if inputCommand[0] in COMMAND_ID.keys():
            return (COMMAND_ID[inputCommand[0]], inputCommand[1:])
        
def getUIChoice():
    '''
    Receives from the user the type of the desired UI 
        1 - command-based
        2 - menu-based
    '''
    while True:
        try:
            ID = getValidNumber(input(UI_PROMPT_TEXT), 'I', 1, 2)
        except:
            pass
    
    if ID == 1:
        return commandBasedUI
    
    print (MENU_UI_TEXT)
    return menuBasedUI

def createStudent(P1, P2, P3):
    '''
    Creates a student with the grades P1, P2, P3, if the data is valid
    @param:
        - P1, P2, P3 - grades of a student
    @return: 
        - a tuple of the form (P1, P2, P3), if the data is valid
        - -1, otherwise
    '''
    try:
        P1 = getValidNumber(P1, 'I')
        P2 = getValidNumber(P2, 'I')
        P3 = getValidNumber(P3, 'I')
    except:
        return -1
    
    return setStudentGrades(P1, P2, P3)
     
def printStudent(student, position):
    '''
    Prints student to console
    @param:
        - student
        - position: student's position in the studentList
    @return: 
        - None
    '''
    P1 = str(getStudentP1(student))
    P2 = str(getStudentP2(student))
    P3 = str(getStudentP3(student))
    print ("Student " + str(position) + ": " + P1 + " | " + P2 + " | " + P3)
    
def printStudentList(studentList):
    '''
    Prints a studentList
    '''
    l = len(studentList)
    
    if l == 0:
        print ("List is empty")
    else:
        for i in range(l):
            printStudent(studentList[i], i)
    
def printStudentByCriteria(studentList, sortedList, count = -1):
    '''
    Prints a re-ordered version of studentList
    @param:
        - studentList = original list of students
        - sortedList = list of students, sorted on a given criterium
        - count = nr of students to be printed
    '''
    if count != -1:
        sortedList = sortedList[: count]
    
    for i in sortedList:
        printStudent(studentList[i[0]], i[0])
    
