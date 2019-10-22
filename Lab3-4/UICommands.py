from UIFunctions import printStudentList, printStudentByAVG, listAllWithProperty, printStudentByGrade
from utilFunctions import getAverage, getMinimum
from validators import isValidKeyword, isValidComparator, isValidNumber, isValidProblem

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
    if l == 0:
        printStudentList(studentList)
            
    elif l == 1:
        if isValidKeyword("sorted", paramList[0]):
            printStudentByAVG(studentList)
        
    elif l == 2:
        sign = isValidComparator(paramList[0])
        score = isValidNumber(paramList[1], 'F', 0, 10)
        if sign != -1 and score != -1:
            listAllWithProperty(sign, score, studentList)
        
    else:
        print ("Invalid number of parameters in \"list\"")

def average(studentList, paramList):
    print (getAverage(studentList, paramList))

def minimumScore(studentList, paramList):
    print (getMinimum(studentList, paramList))
    
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
    
    if l == 1:
        count = isValidNumber(paramList[0], 'I', 1, len(studentList))
        if count == -1:
            return
        printStudentByAVG(studentList, count)
    
    elif l == 2:
        count = isValidNumber(paramList[0], 'I', 1, len(studentList))
        if count == -1:
            return
        
        problem = isValidProblem(paramList[1])
        if problem != -1:
            printStudentByGrade(studentList, count, problem)
    
    else:
        print ("Invalid number of parameters in \"topStudent\"")
        


