from utilFunctions import studentAverage, getAverage, getMinimum
from modifyCommands import add, insert, remove, replace
from setData import createStudent
from getData import *

def studentIsEqualTo(student, P1, P2, P3):
    return getStudentP1(student) == P1 and getStudentP2(student) == P2 and getStudentP3(student) == P3

def testCreateStudent():
    errorMsg = "Failed in createStudent"
    
    s = createStudent(2, 3, 4)
    assert studentIsEqualTo(s, 2, 3, 4), errorMsg
    
    s = createStudent('5', '6', '7')
    assert studentIsEqualTo(s, 5, 6, 7), errorMsg
    
    s = createStudent('11', '9', '3')
    assert s == -1, errorMsg
    
    s = createStudent('a', 'b', 'c')
    assert s == -1, errorMsg

def testAdd():
    errorMsg = "Failed in add"
    studentList = []

    result = add(studentList, [2, 3, 4])
    assert result == 1, errorMsg
    assert len(studentList) == 1, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4), errorMsg

    result = add(studentList, ['a', 2, 5])
    assert result == -1, errorMsg
    assert len(studentList) == 1, errorMsg
    
    result = add(studentList, ['10', '11', '12'])
    assert result == -1, errorMsg
    assert len(studentList) == 1, errorMsg
    
    result = add(studentList, ['0', '3', '3'])
    assert result == 1, errorMsg
    assert len(studentList) == 2, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4), errorMsg
    assert studentIsEqualTo(studentList[1], 0, 3, 3), errorMsg

def testInsert():
    errorMsg = "Failed in insert"
    studentList = []
    
    result = insert(studentList, [1, 2, 3, "at", 0])
    assert result == -1, errorMsg
    assert len(studentList) == 0, errorMsg
    
    studentList.append(createStudent(10, 10, 10))
    result = insert(studentList, [1, 2, 3, "at", 0])
    assert result == 1, errorMsg
    assert len(studentList) == 2, errorMsg
    assert studentIsEqualTo(studentList[0], 1, 2, 3), errorMsg
    assert studentIsEqualTo(studentList[1], 10, 10, 10), errorMsg
    
    result = insert(studentList, [1, 2, 3, "att", 1])
    assert result == -1, errorMsg
    assert len(studentList) == 2, errorMsg
    
    result = insert(studentList, [8, 8, 8, "at", 1])
    assert result == 1, errorMsg
    assert len(studentList) == 3, errorMsg
    assert studentIsEqualTo(studentList[0], 1, 2, 3), errorMsg
    assert studentIsEqualTo(studentList[1], 8, 8, 8), errorMsg
    assert studentIsEqualTo(studentList[2], 10, 10, 10), errorMsg

def testRemove():
    errorMsg = "Failed in remove"
    studentList = []
    
    result = remove(studentList, [0])
    assert result == -1, errorMsg
    assert len(studentList) == 0, errorMsg
    
    studentList.append(createStudent(2, 2, 2))
    result = remove(studentList, [0])
    assert result == 1, errorMsg
    assert len(studentList) == 1, errorMsg
    assert studentIsEqualTo(studentList[0], 0, 0, 0), errorMsg
    
    studentList.append(createStudent(2, 2, 2))
    studentList.append(createStudent(3, 3, 3))
    studentList.append(createStudent(4, 4, 4))
    result = remove(studentList, [1, "to", 2])
    assert result == 1, errorMsg
    assert len(studentList) == 4, errorMsg
    assert studentIsEqualTo(studentList[0], 0, 0, 0)
    assert studentIsEqualTo(studentList[1], 0, 0, 0)
    assert studentIsEqualTo(studentList[2], 0, 0, 0)
    assert studentIsEqualTo(studentList[3], 4, 4, 4)
    
    result = remove(studentList, [3, "too", 3])
    assert result == -1, errorMsg
    assert len(studentList) == 4, errorMsg
    assert studentIsEqualTo(studentList[0], 0, 0, 0)
    assert studentIsEqualTo(studentList[1], 0, 0, 0)
    assert studentIsEqualTo(studentList[2], 0, 0, 0)
    assert studentIsEqualTo(studentList[3], 4, 4, 4)
    
    result = remove(studentList, ['<', 4.1])
    assert result == 1, errorMsg
    assert len(studentList) == 4, errorMsg
    assert studentIsEqualTo(studentList[0], 0, 0, 0)
    assert studentIsEqualTo(studentList[1], 0, 0, 0)
    assert studentIsEqualTo(studentList[2], 0, 0, 0)
    assert studentIsEqualTo(studentList[3], 0, 0, 0)

    result = remove(studentList, ['a', 10])
    assert result == -1, errorMsg
    assert len(studentList) == 4, errorMsg
    assert studentIsEqualTo(studentList[0], 0, 0, 0)
    assert studentIsEqualTo(studentList[1], 0, 0, 0)
    assert studentIsEqualTo(studentList[2], 0, 0, 0)
    assert studentIsEqualTo(studentList[3], 0, 0, 0)

def testReplace():
    errorMsg = "Failed in replace"
    studentList = []
    
    result = replace(studentList, [0, "P2", "with", 10])
    assert result == -1, errorMsg
    assert len(studentList) == 0, errorMsg
    
    studentList.append(createStudent(1, 3, 3))
    result = replace(studentList, [0, "P2", "with", 10])
    assert result == 1, errorMsg
    assert len(studentList) == 1, errorMsg
    assert studentIsEqualTo(studentList[0], 1, 10, 3), errorMsg
    
    result = replace(studentList, [0, "P2", "with", 19])
    assert result == -1, errorMsg
    assert len(studentList) == 1, errorMsg
    assert studentIsEqualTo(studentList[0], 1, 10, 3), errorMsg
    
    result = replace(studentList, [0, "p1", "with", 9])
    assert result == -1, errorMsg
    assert len(studentList) == 1, errorMsg
    assert studentIsEqualTo(studentList[0], 1, 10, 3), errorMsg

def testAverage():
    errorMsg = "Failed in studentAverage"
    studentList = []
    
    studentList.append(createStudent(1, 2, 3))
    result = studentAverage(studentList[0])
    assert result == 2.0, errorMsg
    assert studentIsEqualTo(studentList[0], 1, 2, 3), errorMsg
    assert len(studentList) == 1, errorMsg
    
    studentList.append(createStudent(10, 4, 2))
    result = studentAverage(studentList[1])
    assert result == 5.333, errorMsg
    assert studentIsEqualTo(studentList[1], 10, 4, 2), errorMsg
    assert len(studentList) == 2, errorMsg
    
    studentList.append(createStudent(0, 0, 0))
    result = studentAverage(studentList[2])
    assert result == 0.0, errorMsg
    assert studentIsEqualTo(studentList[2], 0, 0, 0), errorMsg
    assert len(studentList) == 3, errorMsg

def testAverageRange():
    errorMsg = "Failed in getAverage"
    studentList = []
    
    result = getAverage(studentList, [0, "to", 0])
    assert result == -1, errorMsg
    assert len(studentList) == 0, errorMsg
    
    studentList.append(createStudent(2, 3, 4))
    result = getAverage(studentList, [0, "to", 0])
    assert result == 3, errorMsg
    assert len(studentList) == 1, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    
    studentList.append(createStudent(10, 10, 10))
    studentList.append(createStudent(9, 9, 8))
    result = getAverage(studentList, [0, "to", 2])
    assert result == 7.222, errorMsg
    assert len(studentList) == 3, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    assert studentIsEqualTo(studentList[1], 10, 10, 10)
    assert studentIsEqualTo(studentList[2], 9, 9, 8)
    
    result = getAverage(studentList, [2, "to", 0])
    assert result == -1, errorMsg
    assert len(studentList) == 3, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    assert studentIsEqualTo(studentList[1], 10, 10, 10)
    assert studentIsEqualTo(studentList[2], 9, 9, 8)

def testMinRange():
    errorMsg = "Failed in getMinimum"
    studentList = []
    
    result = getMinimum(studentList, [0, "to", 0])
    assert result == -1, errorMsg
    assert len(studentList) == 0, errorMsg

    studentList.append(createStudent(2, 3, 4))
    studentList.append(createStudent(8, 9, 10))
    studentList.append(createStudent(9, 9, 10))
    result = getMinimum(studentList, [0, "to", 2])
    assert result == 3, errorMsg
    assert len(studentList) == 3, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4), errorMsg
    assert studentIsEqualTo(studentList[1], 8, 9, 10), errorMsg
    assert studentIsEqualTo(studentList[2], 9, 9, 10), errorMsg
    
    result = getMinimum(studentList, [1, "to", 1])
    assert result == 9, errorMsg
    assert len(studentList) == 3, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4), errorMsg
    assert studentIsEqualTo(studentList[1], 8, 9, 10), errorMsg
    assert studentIsEqualTo(studentList[2], 9, 9, 10), errorMsg
    
    result = getMinimum(studentList, [2, "to", 1])
    assert result == -1, errorMsg
    assert len(studentList) == 3, errorMsg
    assert studentIsEqualTo(studentList[0], 2, 3, 4), errorMsg
    assert studentIsEqualTo(studentList[1], 8, 9, 10), errorMsg
    assert studentIsEqualTo(studentList[2], 9, 9, 10), errorMsg

def testFunction():
    testCreateStudent()
    testAdd()
    testInsert()
    testRemove()
    testReplace()
    testAverage()
    testAverageRange()
    testMinRange()

testFunction()

