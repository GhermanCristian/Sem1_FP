'''
The commands which are strictly UI
'''

from UIFunctions import printStudentList, printStudentByCriteria
from nonUIFunctions import getAverage, getMinimum, filterProperty,\
    sortStudentGradesAVG, sortStudentGradesPx
from validators import isValidKeyword, getValidComparator, getValidNumber, getValidProblem,\
    isValidParamLen, getValidPosition
from customExceptions import ParamError

def listStudents(studentList, paramList):
    '''
    Interface for the list functions
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - in this case there are multiple sets of parameters
    @return:
        - None
    '''
    l = len(paramList)
    
    try:
        if l > 2:
            raise ParamError("Invalid number of parameters in \"list\"")
    
    except ParamError:
        return
    
    if l == 0:
        printStudentList(studentList)
            
    elif l == 1:
        try:
            isValidKeyword("sorted", paramList[0])
        
        except:
            return 
        
        sortedList = sortStudentGradesAVG(studentList)
        printStudentByCriteria(studentList, sortedList)
        
    elif l == 2:
        try:
            sign = getValidComparator(paramList[0])
            score = getValidNumber(paramList[1], 'F', 0, 10)
        
        except:
            return

        printStudentList(filterProperty(sign, score, studentList))

def average(studentList, paramList):
    '''
    Prints the average of the average score in a given range
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - startPos
            - "to" keyword
            - endPos
    '''
    try:
        isValidParamLen(3, len(paramList))
        startPos = getValidPosition(paramList[0], studentList)
        endPos = getValidPosition(paramList[2], studentList)
        isValidKeyword("to", paramList[1])
        
        if startPos > endPos:
            raise ArithmeticError("Start position is larger than the end position")
        
    except:
        return 
    
    print (getAverage(studentList, startPos, endPos))

def minimumScore(studentList, paramList):
    '''
    Prints the minimum average score in a given range
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - startPos
            - "to" keyword
            - endPos
    '''
    try:
        isValidParamLen(3, len(paramList))
        startPos = getValidPosition(paramList[0], studentList)
        endPos = getValidPosition(paramList[2], studentList)
        isValidKeyword("to", paramList[1])
        
        if startPos > endPos:
            raise ArithmeticError("Start position is larger than the end position")
        
    except:
        return
    
    print (getMinimum(studentList, startPos, endPos))
    
def topStudent(studentList, paramList):
    '''
    Prints the top students, based on their average score or the score for a particular problem
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - in this case there are multiple sets of parameters
    @return:
        - None
    '''
    l = len(paramList)
    
    try:
        if l == 0 or l > 2:
            raise ParamError("Invalid number of parameters in \"topStudent\"")
        
    except:
        return
    
    if l == 1:
        try:
            count = getValidNumber(paramList[0], 'I', 1, len(studentList))
            
        except:
            return
        
        sortedList = sortStudentGradesAVG(studentList)
        printStudentByCriteria(studentList, sortedList, count)
    
    elif l == 2:
        try:
            count = getValidNumber(paramList[0], 'I', 1, len(studentList))
            problem = getValidProblem(paramList[1])
        
        except:
            return
        
        sortedList = sortStudentGradesPx(studentList, problem)
        printStudentByCriteria(studentList, sortedList, count)
        


