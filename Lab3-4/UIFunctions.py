'''
UI functions which are not commands, but are used by them
- the first 2 functions deal with data input
'''

from validators import getValidNumber
from interact import *
from constants import UI_PROMPT_TEXT, MENU_UI_TEXT
from customExceptions import InputTypeError
from re import *
        
def getUIChoice(UI_TYPE_PATTERN, COM_patternList, MEN_patternList):
    '''
    Receives from the user the type of the desired UI 
        1 - command-based (regex pattern for commands)
        2 - menu-based (regex pattern for menu)
    @param:
        - UI_TYPE_PATTERN = 1 or 2
        - COM_patternList = regex patterns for commands
        - MEN_patternList = regex patterns for menu
    @return:
        - patternList = one of the above pattern lists
    '''
    while True:
        ID = input(UI_PROMPT_TEXT)
        #I don't know why eclipse shows this line has an error (?)
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
        return COM_patternList
    
    print (MENU_UI_TEXT)
    return MEN_patternList

def getAction(patternList):
    '''
    Gets user input, which is checked against a regular expression
    @param:
        - patternList = list of regex patterns (either command or menu-based)
    @return:
        - tuple of the form (commandID, action arguments)
    '''
    #maps idx to commandID (because "remove", for example, has 3 variations)
    commandID = [0, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9]
    while True:
        inputAction = input("Please insert the command and the arguments: ")
          
        for idx in range(len(patternList)):
            pattern = patternList[idx]
            #I don't know why eclipse shows this line has an error (?)
            regex = compile(pattern, VERBOSE | IGNORECASE)
            result = fullmatch(regex, inputAction)
            
            if result != None:
                return (commandID[idx], result.groups()[1:])
           
        #if the program reaches this point, it means the input was invalid 
        try:
            raise InputTypeError("Invalid input")
        except:
            continue

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
    
