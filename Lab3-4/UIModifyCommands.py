'''
The interface of functions that modify the list
- they can take invalid input
'''

from validators import isValidKeyword, isValidParamLen, getValidComparator, getValidNumber, \
                       getValidPosition, getValidProblem
from nonUIFunctions import studentIsEqualTo
from nonUIImplementation import add, insert, removeAllWithProperty, removePosition, removeRange, replace, undo
from customExceptions import EmptyPositionError, ParamError, RangeError
from UIFunctions import createStudent

def addUI(studentList, paramList):
    '''
    Interface for the 'add' function
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - 3 integers between 0 and 10 = the three grades of a student
    @return:
        - None, if the input is valid
        - -1, otherwise
    '''
    try:
        isValidParamLen(3, len(paramList))
        student = createStudent(paramList[0], paramList[1], paramList[2]) #if invalid raises exception
        
    except:
        return -1 
    
    add(studentList, student)
    
def insertUI(studentList, paramList):
    '''
    Interface for the 'insert' function
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - 3 intgers between 0 and 10
            - "at" keyword
            - position at which to insert the value (integer)
    @return:
        - None, if the input is valid
        - -1, otherwise
    '''
    try:
        isValidParamLen(5, len(paramList))
        isValidKeyword("at", paramList[3])
        position = getValidPosition(paramList[4], studentList)
        student = createStudent(paramList[0], paramList[1], paramList[2])
        
    except:
        return -1
    
    insert(studentList, position, student)

def removeUI(studentList, paramList):
    '''
    Interface for the 'remove' functions
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - in this case there are multiple sets of parameters
    @return:
        - None, if the input is valid
        - -1, otherwise
    '''
    l = len(paramList)
    
    try:
        if l > 3 or l == 0:
            raise ParamError("Invalid number of parameters")
    
    except ParamError:
        return -1 
    
    if l == 1:
        try:
            position = getValidPosition(paramList[0], studentList)
    
        except:
            return -1
        
        removePosition(position, studentList)
    
    elif l == 2:
        try:
            sign = getValidComparator(paramList[0])
            score = getValidNumber(paramList[1], 'F')
        
        except:
            return -1
        
        removeAllWithProperty(sign, score, studentList)
    
    else:
        try:
            startPos = getValidPosition(paramList[0], studentList)
            endPos = getValidPosition(paramList[2], studentList)
            if startPos > endPos:
                raise RangeError("Start position is larger than the end position")
            isValidKeyword(paramList[1], "to")
        
        except:
            return -1
        
        removeRange(startPos, endPos, studentList)

def replaceUI(studentList, paramList):
    '''
    Interface for the 'replace' function
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - position of the student to be replaced (integer)
            - Px = which grade to change (string)
            - "with" keyword
            - grade to replace Px with
    @return:
        - None, if the input is valid
        - -1, otherwise
    '''
    try:
        isValidParamLen(4, len(paramList))
        position = getValidPosition(paramList[0], studentList)
        isValidKeyword("with", paramList[2])
        grade = getValidNumber(paramList[3], 'I')
        problem = getValidProblem(paramList[1])
        
        if studentIsEqualTo(studentList[position], 0, 0, 0):
            raise EmptyPositionError("Cannot replace an empty position")
        
    except:
        return -1
    
    replace(studentList, position, problem, grade)
    
def undoUI(studentList, paramList, commandStack):
    '''
    Interface for the 'undo' function
    @param:
        - studentList = list of students
        - commandStack = list of all previous list states
    @return:
        - None, if the input is valid
        - -1, otherwise
    '''
    try:
        isValidParamLen(0, len(paramList))
        
        if len(commandStack) == 0:
            raise EmptyPositionError("No moves left - history stack is empty")
        
    except:
        return -1

    undo(studentList, commandStack)
