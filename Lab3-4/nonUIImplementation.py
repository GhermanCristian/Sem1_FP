'''
The implementation of the commands which modify the studentList
- they can't take invalid input
'''

from nonUIFunctions import studentAverage
from interact import *

def add(studentList, student):
    '''
    Adds a student to the end of studentList
    @param:
        - studentList = list of students
        - student
    @return:
        - None
    '''        
    studentList.append(student)
    
def insert(studentList, position, student):
    '''
    Inserts a student in the studentList at a specified position
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - 3 intgers between 0 and 10
            - "at" keyword
            - position at which to insert the value (integer) - already validated
    @return:
        - None
    '''
    studentList.insert(position, student)

def removePosition(position, studentList):
    '''
    Sets the score at 'position' from studentList to (0, 0, 0)
    @param:
        - position = integer; the position of the student
        - studentList = list of students
    @return:
        - None
    '''
    studentList.insert(position, setStudentGrades(0, 0, 0))
    studentList.pop(position + 1)

def removeAllWithProperty(sign, score, studentList):
    '''
    Sets the score of all students with a property to 0 
    @param:
        - sign = integer representing the type of comparator
            - 0: a == b
            - 1: a > b
            - 2: a < b 
        - score = integer representing the average score to compare with
        - studentList = list of students
    @return:
        - None
    '''
    for i in range(len(studentList)):
        averageScore = studentAverage(studentList[i])
        if     (sign == 0 and averageScore == score) \
            or (sign == 1 and averageScore > score)  \
            or (sign == 2 and averageScore < score):
            removePosition(i, studentList)

def removeRange(startPos, endPos, studentList):
    '''
    Sets the score at all positions between (startPos, endPos) from studentList to (0, 0, 0)
    @param:
        - startPos = integer; the position of the first student in the range
        - endPos = integer; the position of the last student in the range
        - studentList = list of students
    @return:
        - None
    '''
    for i in range(startPos, endPos + 1):
        removePosition(i, studentList)

def replace(studentList, position, problem, grade):
    '''
    Replaces score obtained by student
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - position = integer, position of student to be replaced 
            - problem = intger, problem whose score has to be replaced
            - grade = integer, new grade
    @return:
        - None
    '''

    student = studentList[position]
                    
    P1 = getStudentP1(student)
    P2 = getStudentP2(student)
    P3 = getStudentP3(student)
                    
    if problem == 1:
        P1 = grade
    elif problem == 2:
        P2 = grade
    else:
        P3 = grade
    
    #we know that P1,2,3 are valid, so no need to use createStudent (which checks input)
    student = setStudentGrades(P1, P2, P3)  
    studentList.insert(position, student)
    studentList.pop(position + 1)
        
def undo(studentList, commandStack):
    '''
    Undoes the last command which has modified the studentList
    @param:
        - studentList = list of students
        - commandStack = list of all previous list states
    @return:
        - None
    '''
    studentList.clear()
    studentList.extend(commandStack.pop())

