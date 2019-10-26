'''
UI functions which are not commands, but are used by them
- the first 3 functions deal with data input
'''

from validators import getValidNumber
from interact import *
from constants import UI_PROMPT_TEXT, MENU_UI_TEXT
from customExceptions import ParamError, InputTypeError
from re import *
from regexPatterns import UI_TYPE_PATTERN

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
        
        try:
            if len(inputCommand) == 0:
                raise ParamError("Invalid command")
        except:
            continue
        
        inputCommand.strip()
        inputCommand = inputCommand.split()
            
        try:
            commandID = getValidNumber(inputCommand[0], 'I', 0, 9)
        except:
            continue

        return (commandID, inputCommand[1:])

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
            continue
        
        inputCommand.strip()
        inputCommand = inputCommand.split()
        inputCommand[0] = inputCommand[0].lower()
            
        try:
            if inputCommand[0] not in COMMAND_ID.keys():
                raise InputTypeError("Invalid command")
        except:
            continue
        
        return (COMMAND_ID[inputCommand[0]], inputCommand[1:])
        
def getAction(COM_patternList, studentList):
    '''
    '''
    while True:
        inputAction = input("Please insert the command and the arguments: ")
          
        for idx in range(len(COM_patternList)):
            pattern = COM_patternList[idx]
            regex = compile(pattern, VERBOSE | IGNORECASE)
            result = fullmatch(regex, inputAction)
            
            if result != None:
                pass
                #return (idx, getParams[idx](studentList)) - getparams is a list of validators
            
        try:
            raise InputTypeError("Invalid input")
        except:
            continue

def getUIChoice():
    '''
    Receives from the user the type of the desired UI 
        1 - command-based
        2 - menu-based
    '''
    while True:
        ID = input(UI_PROMPT_TEXT)
        UITypeRegex = compile(UI_TYPE_PATTERN, VERBOSE | IGNORECASE)
        result = fullmatch(UITypeRegex, ID)
        
        try:
            if result == None:
                raise InputTypeError("Invalid number")
            break
        except:
            continue
        
    ID = int(result.group(1))
    
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
    
