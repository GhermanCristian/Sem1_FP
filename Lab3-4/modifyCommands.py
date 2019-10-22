from utilFunctions import removeAllWithProperty, removePosition, removeRange
from getData import *
from setData import createStudent
from validators import isValidKeyword, isValidPosition, isValidComparator, isValidNumber

def add(studentList, paramList, position = -1):
    '''
    Adds a student in the list at a specified position (by default - at the end of the list)
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - 3 integers between 0 and 10 = the three grades of a student
    @return:
        - 1, if the function worked 
        - -1, otherwise
    '''
    if len(paramList) != 3:
        print ("Incorrect number of parameters in \"add\"")
        return -1
    
    student = createStudent(paramList[0], paramList[1], paramList[2])
    if student == -1:
        return -1
            
    if position == -1:
        #actual "add"
        studentList.append(student)
    else:
        #insert
        P1 = getStudentP1(studentList[position])
        P2 = getStudentP2(studentList[position])
        P3 = getStudentP3(studentList[position])
        studentList.insert(position, student)
                    
        if P1 == P2 == P3 == 0:
            studentList.pop(position + 1)
                    
    return 1 #success
    
def insert(studentList, paramList):
    '''
    Inserts a student in the studentList at a specified position
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - 3 intgers between 0 and 10
            - "at" keyword
            - position at which to insert the value (integer)
    @return:
        - 1, if the function worked 
        - -1, otherwise
    '''
    if len(paramList) != 5:
        print ("Incorrect number of parameters in \"insert\"")
        return -1
    if not isValidKeyword("at", paramList[3]):
        return -1
        
    position = isValidPosition(paramList[4], studentList)
    if position == -1:
        return -1

    add(studentList, paramList[:3], position)
    return 1 #success

def remove(studentList, paramList):
    '''
    Interface for the remove functions
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - in this case there are multiple sets of parameters
    @return:
        - 1, if the function worked correctly
        - -1, otherwise
    '''
    l = len(paramList)
    if l == 1:
        position = isValidPosition(paramList[0], studentList)
        if position != -1:
            removePosition(position, studentList)
        else:
            return -1
            
    elif l == 2:
        sign = isValidComparator(paramList[0])
        score = isValidNumber(paramList[1], 'F')
        if sign != -1 and score != -1:
            removeAllWithProperty(sign, score, studentList)
        else:
            return -1
        
    elif l == 3:
        startPos = isValidPosition(paramList[0], studentList)
        endPos = isValidPosition(paramList[2], studentList)
        
        if startPos != -1 and endPos != -1:
            if startPos > endPos:
                print ("Start position is larger than the end position")
                return -1
        
            if isValidKeyword(paramList[1], "to"):
                removeRange(startPos, endPos, studentList)
                
            else:
                return -1

    else:
        print ("Invalid number of parameters in \"remove\"")
        return -1
    
    return 1   

def replace(studentList, paramList):
    '''
    Replaces score obtained by student
    @param:
        - studentList = list of students
        - paramList = list of parameters
            - position of the student to be replaced (integer)
            - Px = which grade to change (string)
            - "with" keyword
            - grade to replace Px with
    @return:
        - 1, if the function worked
        - -1, otherwise
    '''
    if len(paramList) != 4:
        print ("Invalid number of paramters")
        return -1
    
    position = isValidPosition(paramList[0], studentList)
    if position == -1:
        return -1
    if not isValidKeyword("with", paramList[2]):
        return -1
    grade = isValidNumber(paramList[3], 'I')
    if grade == -1:
        return -1
    student = studentList[position]
                    
    P1 = getStudentP1(student)
    P2 = getStudentP2(student)
    P3 = getStudentP3(student)
                    
    if P1 == P2 == P3 == 0:
        print ("Cannot replace an empty position")
        return -1
                    
    if paramList[1] == "P1":
        P1 = grade
    elif paramList[1] == "P2":
        P2 = grade
    elif paramList[1] == "P3":
        P3 = grade
    else:
        print ("Invalid Px")
        return -1
                    
    student = createStudent(P1, P2, P3)  
    studentList.insert(position, student)
    studentList.pop(position + 1)
    return 1 #success
        
def undo(studentList, paramList, commandStack):
    '''
    Undoes the last command which has modified the studentList
    @param:
        - studentList = list of students
        - paramList = list of parameters
        - commandStack = list of all previous list states
    @return:
        - the last list state, if the stack is non-empty
        - studentList, if the stack is empty
        - -1 if the function failed (incorrect input)
    '''
    if len(paramList) != 0:
        print ("Incorrect number of parameters in \"undo\"")
        return -1
    
    if len(commandStack) > 0:
        return commandStack.pop()[:]
    
    print ("No moves left")
    return studentList[:]

