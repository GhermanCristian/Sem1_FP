'''
Multi-purpose, non-UI module
'''

from interact import getStudentP1, getStudentP2, getStudentP3

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
    
def getAverage(studentList, startPos, endPos):
    '''
    Computes the average of the average score in a given range
    @param:
        - studentList = list of students
        - startPos = first position in range
        - endPos = last position in range
    @return:
        - average of the average score (float)
    '''
    gradeSum = 0
    for i in studentList[startPos : endPos + 1]:
        gradeSum += studentAverage(i)
    
    return int((gradeSum / (endPos + 1 - startPos)) * 1000) / 1000
    
def getMinimum(studentList, startPos, endPos):    
    '''
    Computes the minimum of the average scores in a given range
    @param:
        - studentList = list of students
        - startPos = first position in range
        - endPos = last position in range
    @return:
        - minimum of the average score (float)
    '''
    minValue = 11
    for i in studentList[startPos : endPos + 1]:
        average = studentAverage(i)
        if minValue > average:
            minValue = average
            
    return (minValue)

def filterProperty(sign, score, studentList):
    '''
    Returns a list of students whose average corresponds to the expression "< = > value"
    @param:
        - sign = integer representing the type of comparation
            - 0: a == b
            - 1: a > b
            - 2: a < b 
        - score = integer representing the average score to compare with
        - studentList = list of students
    @return:
        - filteredList = list of students with the above property
    '''
    filteredList = []
    
    for i in range(len(studentList)):
        averageScore = studentAverage(studentList[i])
        if     (sign == 0 and averageScore == score) \
            or (sign == 1 and averageScore > score)  \
            or (sign == 2 and averageScore < score):
                filteredList.append(studentList[i])
                
    return filteredList

def studentIsEqualTo(student, P1, P2, P3):
    '''
    Checks if a student's grades are equal to (P1, P2, P3)
    @param:
        - student
        - P1, P2, P3 = integers, valid grades
    @return:
        - True, if the student's grades are equal to (P1, P2, P3)
        - False, otherwise
    '''
    return getStudentP1(student) == P1 and getStudentP2(student) == P2 and getStudentP3(student) == P3


    