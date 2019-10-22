from getData import getStudentP1, getStudentP2, getStudentP3
from setData import createStudent
from validators import isValidKeyword, isValidPosition

def removePosition(position, studentList):
    '''
    Sets the score at 'position' from studentList to (0, 0, 0)
    @param:
        - position = integer; the position of the student
        - studentList = list of students
    @return:
        - None
    '''
    studentList.insert(position, createStudent(0, 0, 0))
    studentList.pop(position + 1)

def removeAllWithProperty(sign, score, studentList):
    '''
    Sets the score of all students with a property to 0 
    @param:
        - sign = integer representing the type of comparation
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
            
def studentAverage(student):
    '''
    Calculates the average of a student's grades
    @param:
        - student
    @return:
        - arithmetic average of a student's scores
    '''
    gradeSum = int(getStudentP1(student)) + int(getStudentP2(student)) + int(getStudentP3(student))
    return int(gradeSum / 3 * 1000) / 1000

def sortKeyAVG(element):
    return element[1]

def sortStudentGradesAVG(studentList):
    '''
    Sorts a studentList (descending) by the average grade
    @param:
        - studentList = list of students
    @return:
        - studentAVG = list of tuples (i, averageOfStudentI), sorted in decreasing order
    '''
    studentAVG = []
    for i in range(len(studentList)):
        studentAVG.append((i, studentAverage(studentList[i])))
    studentAVG.sort(key = sortKeyAVG, reverse = True)    
    
    return studentAVG

def sortKeyProblem(element):
    return element[1]

def sortStudentGradesPx(studentList, problem):
    '''
    Sorts a studentList (descending) by the score obtained on a particular problem
    @param:
        - studentList = list of students
        - problem = problem from the set {P1, P2, P3}
    @return:
        - studentGrades = sorted list of students
    '''
    studentGrades = []
    
    for i in range(len(studentList)):
        if problem == 1:
            studentGrades.append((i, getStudentP1(studentList[i])))
        elif problem == 2:
            studentGrades.append((i, getStudentP2(studentList[i])))
        else:
            studentGrades.append((i, getStudentP3(studentList[i])))
            
    studentGrades.sort(key = sortKeyProblem, reverse = True)
    
    return studentGrades    
    
def getAverage(studentList, paramList):
    '''
    Computes the average of the average score in a given range
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - startPos = first position in range
            - "to" keyword
            - endPos = last position in range
    @return:
        - -1, if the parameters are invalid
        - average of average grade in given range, otherwise
    '''
    if len(paramList) != 3:
        return -1
    
    startPos = isValidPosition(paramList[0], studentList)
    endPos = isValidPosition(paramList[2], studentList)
    if startPos == -1 or endPos == -1:
        return -1
    if not isValidKeyword("to", paramList[1]):
        return -1
    
    if startPos > endPos:
        print ("Start position is larger than the end position")
        return -1
    
    gradeSum = 0
    for i in studentList[startPos : endPos + 1]:
        gradeSum += studentAverage(i)
    
    return int((gradeSum / (endPos + 1 - startPos)) * 1000) / 1000
    
def getMinimum(studentList, paramList):    
    '''
    Computes the minimum of the average scores in a given range
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - startPos = first position in range
            - "to" keyword
            - endPos = last position in range
    @return:
        - -1, if the parameters are invalid
        - minValue = integer equal to the minimum average grade in the range, else
    '''
    if len(paramList) != 3:
        return -1
    
    startPos = isValidPosition(paramList[0], studentList)
    endPos = isValidPosition(paramList[2], studentList)
    if startPos == -1 or endPos == -1:
        return -1
    if not isValidKeyword("to", paramList[1]):
        return -1
    
    if startPos > endPos:
        print ("Start position is larger than the end position")
        return -1
    
    minValue = 11
    for i in studentList[startPos : endPos + 1]:
        average = studentAverage(i)
        if minValue > average:
            minValue = average
            
    return (minValue)

    
    