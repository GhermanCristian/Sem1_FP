from nonUIFunctions import studentAverage, getAverage, getMinimum, filterProperty, studentIsEqualTo
from nonUIImplementation import add, insert, removePosition, removeAllWithProperty, removeRange, replace
from UIFunctions import createStudent
from exampleLists import exampleList2, exampleList3
from validators import isValidKeyword, isValidParamLen, getValidComparator, getValidNumber, \
                       getValidPosition, getValidProblem

'''
ALl the functions (with the exception of validators), need to have valid input
- error messages will be printed by testValidators, when inputting invalid data
'''

def testCreateStudent():
    s = createStudent(2, 3, 4)
    assert studentIsEqualTo(s, 2, 3, 4)
    
    s = createStudent(5, 6, 7)
    assert studentIsEqualTo(s, 5, 6, 7)
    
def testAdd():
    studentList = []

    add(studentList, createStudent(2, 3, 4))
    assert len(studentList) == 1
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    
    add(studentList, createStudent(0, 3, 3))
    assert len(studentList) == 2
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    assert studentIsEqualTo(studentList[1], 0, 3, 3)

def testInsert():
    studentList = []
    
    studentList.append(createStudent(10, 10, 10))
    insert(studentList, 0, createStudent(1, 2, 3))
    assert len(studentList) == 2
    assert studentIsEqualTo(studentList[0], 1, 2, 3)
    assert studentIsEqualTo(studentList[1], 10, 10, 10)
    
    insert(studentList, 1, createStudent(8, 8, 8))
    assert len(studentList) == 3
    assert studentIsEqualTo(studentList[0], 1, 2, 3)
    assert studentIsEqualTo(studentList[1], 8, 8, 8)
    assert studentIsEqualTo(studentList[2], 10, 10, 10)

def testRemove():
    studentList = []
    
    studentList.append(createStudent(2, 2, 2))
    removePosition(0, studentList)
    assert len(studentList) == 1
    assert studentIsEqualTo(studentList[0], 0, 0, 0)
    
    studentList.append(createStudent(2, 2, 2))
    studentList.append(createStudent(3, 3, 3))
    studentList.append(createStudent(4, 4, 4))
    removeRange(1, 2, studentList)
    assert len(studentList) == 4
    assert studentIsEqualTo(studentList[0], 0, 0, 0)
    assert studentIsEqualTo(studentList[1], 0, 0, 0)
    assert studentIsEqualTo(studentList[2], 0, 0, 0)
    assert studentIsEqualTo(studentList[3], 4, 4, 4)
    
    removeAllWithProperty(2, 4.1, studentList)
    assert len(studentList) == 4
    assert studentIsEqualTo(studentList[0], 0, 0, 0)
    assert studentIsEqualTo(studentList[1], 0, 0, 0)
    assert studentIsEqualTo(studentList[2], 0, 0, 0)
    assert studentIsEqualTo(studentList[3], 0, 0, 0)

def testReplace():
    studentList = []
    
    studentList.append(createStudent(1, 3, 3))
    replace(studentList, 0, 2, 10)
    assert len(studentList) == 1
    assert studentIsEqualTo(studentList[0], 1, 10, 3)

def testAverage():
    studentList = []
    
    studentList.append(createStudent(1, 2, 3))
    result = studentAverage(studentList[0])
    assert result == 2.0
    assert studentIsEqualTo(studentList[0], 1, 2, 3)
    assert len(studentList) == 1
    
    studentList.append(createStudent(10, 4, 2))
    result = studentAverage(studentList[1])
    assert result == 5.333
    assert studentIsEqualTo(studentList[1], 10, 4, 2)
    assert len(studentList) == 2
    
    studentList.append(createStudent(0, 0, 0))
    result = studentAverage(studentList[2])
    assert result == 0.0
    assert studentIsEqualTo(studentList[2], 0, 0, 0)
    assert len(studentList) == 3

def testAverageRange():
    studentList = []
    
    studentList.append(createStudent(2, 3, 4))
    result = getAverage(studentList, 0, 0)
    assert result == 3
    assert len(studentList) == 1
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    
    studentList.append(createStudent(10, 10, 10))
    studentList.append(createStudent(9, 9, 8))
    result = getAverage(studentList, 0, 2)
    assert result == 7.222
    assert len(studentList) == 3
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    assert studentIsEqualTo(studentList[1], 10, 10, 10)
    assert studentIsEqualTo(studentList[2], 9, 9, 8)

def testMinRange():
    studentList = []
    
    studentList.append(createStudent(2, 3, 4))
    studentList.append(createStudent(8, 9, 10))
    studentList.append(createStudent(9, 9, 10))
    result = getMinimum(studentList, 0, 2)
    assert result == 3
    assert len(studentList) == 3
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    assert studentIsEqualTo(studentList[1], 8, 9, 10)
    assert studentIsEqualTo(studentList[2], 9, 9, 10)
    
    result = getMinimum(studentList, 1, 1)
    assert result == 9
    assert len(studentList) == 3
    assert studentIsEqualTo(studentList[0], 2, 3, 4)
    assert studentIsEqualTo(studentList[1], 8, 9, 10)
    assert studentIsEqualTo(studentList[2], 9, 9, 10)

def testFilter():
    studentList = exampleList2

    filteredList = filterProperty(2, 5, studentList)
    assert len(filteredList) == 3
    assert studentIsEqualTo(filteredList[0], 3, 4, 4)
    assert studentIsEqualTo(filteredList[1], 4, 4, 2)
    assert studentIsEqualTo(filteredList[2], 6, 5, 1)
    
    filteredList = filterProperty(1, 10, studentList)
    assert len(filteredList) == 0
    
    studentList = exampleList3
    
    filteredList = filterProperty(1, 4.95, studentList)
    assert len(filteredList) == 5
    assert studentIsEqualTo(filteredList[0], 8, 10, 10)
    assert studentIsEqualTo(filteredList[1], 0, 9, 9)
    assert studentIsEqualTo(filteredList[2], 2, 6, 8)
    assert studentIsEqualTo(filteredList[3], 8, 6, 1)
    assert studentIsEqualTo(filteredList[4], 2, 9, 6)
    
    filteredList = filterProperty(0, 6, studentList)
    assert len(filteredList) == 1
    assert studentIsEqualTo(filteredList[0], 0, 9, 9)

def testValidators():
    #correct input, shouldn't raise any exceptions
    try:
        isValidKeyword("word", "word")
        isValidParamLen(3, 3)
        
        x = getValidComparator("<")
        assert x == 2
        x = getValidComparator("=")
        assert x == 0
        x = getValidComparator(">")
        assert x == 1
        
        x = getValidNumber("123", 'I', 0, 150)
        assert x == 123
        x = getValidNumber("7", 'I')
        assert x == 7
        x = getValidNumber("12.05", 'F', 0, 15)
        assert x == 12.05
        x = getValidNumber("1.02", 'F')
        assert x == 1.02
        x = getValidNumber(4, 'I')
        assert x == 4
        x = getValidNumber(4.1, 'F')
        assert x == 4.1
        
        studentList = []
        studentList.append(createStudent(0, 0, 0))
        x = getValidPosition("0", studentList)
        assert x == 0
        studentList.append(createStudent(0, 0, 0))
        studentList.append(createStudent(0, 0, 0))
        studentList.append(createStudent(0, 0, 0))
        studentList.append(createStudent(0, 0, 0))
        x = getValidPosition("3", studentList)
        assert x == 3
        
        x = getValidProblem("P1")
        assert x == 1
        x = getValidProblem("P2")
        assert x == 2
        x = getValidProblem("P3")
        assert x == 3
        
        assert True
        
    except:
        assert False
        
    #incorrect input
    try:
        isValidKeyword("word", "woord")
    except:
        assert True
        
    try:
        isValidParamLen(3, 5)
    except:
        assert True
        
    try:
        x = getValidComparator("x")
    except:
        assert True
        
    try:
        x = getValidNumber("12a", "I", 0, 15)
    except:
        assert True
        
    try:
        x = getValidNumber("12", "I")
    except:
        assert True
        
    try:
        x = getValidNumber("12.1", "I")
    except:
        assert True
        
    try:
        x = getValidNumber("12.1", "F")
    except:
        assert True
        
    try:
        x = getValidPosition(0, [])
    except:
        assert True
        
    try:
        studentList = []
        studentList.append(createStudent(0, 0, 0))
        studentList.append(createStudent(0, 0, 0))
        studentList.append(createStudent(0, 0, 0))
        x = getValidPosition(3, [])
    except:
        assert True

def testFunction():
    testCreateStudent()
    testAdd()
    testInsert()
    testRemove()
    testReplace()
    testAverage()
    testAverageRange()
    testMinRange()
    testFilter()
    testValidators()

testFunction()

