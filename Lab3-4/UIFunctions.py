from validators import isValidNumber
from utilFunctions import studentAverage, sortStudentGradesAVG, sortStudentGradesPx
from getData import *
from constants import UI_PROMPT_TEXT, MENU_UI_TEXT

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
            
            commandID = isValidNumber(inputCommand[0], 'I', 0, 9)
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
        
        if len(inputCommand) > 0:
            inputCommand.strip()
            inputCommand = inputCommand.split()
            #command name (add, insert etc.)
            inputCommand[0] = inputCommand[0].lower()
            
            if inputCommand[0] in COMMAND_ID.keys():
                #inputCommand[1:] = the other parameters (from "add 2 3 4", this is "2, 3, 4")
                return (COMMAND_ID[inputCommand[0]], inputCommand[1:])
        
        print ("Invalid command")
        
def getUIChoice():
    while True:
        ID = isValidNumber(input(UI_PROMPT_TEXT), 'I', 1, 2)
        if ID != -1:
            break
    
    if ID == 1:
        return commandBasedUI
    
    print (MENU_UI_TEXT)
    return menuBasedUI
        
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
    l = len(studentList)
    
    if l == 0:
        print ("List is empty")
    else:
        for i in range(l):
            printStudent(studentList[i], i)

def printStudentByAVG(studentList, count = -1):
    '''
    Prints a re-ordered list of students, with their original ID
    @param:
        - studentList = list of students
        - count = number of students to be printed (if -1 => the entire list)
    @return:
        - None
    '''
    studentAVG = sortStudentGradesAVG(studentList)
    
    if count != -1:
        del studentAVG[count: ]
    
    for i in studentAVG:
        printStudent(studentList[i[0]], i[0])
        
def printStudentByGrade(studentList, count, problem):
    '''
    Prints the first 'count' students based on their score on 'problem', with their original ID
    @param:
        - studentList = list of students
        - count = nr of students to be printed
        - problem = 
    @return:
        - None
    '''
    studentGrade = sortStudentGradesPx(studentList, problem)
    
    del studentGrade[count: ]
    
    for i in studentGrade:
        printStudent(studentList[i[0]], i[0])
    

