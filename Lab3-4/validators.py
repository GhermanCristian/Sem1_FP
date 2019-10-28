'''
Functions which validate various input values and which raise exceptions
'''

from customExceptions import RangeError, InputTypeError

def getValidPosition(position, studentList):
    '''
    Checks if 'position' is valid within the current studentList
    @param:
        - position = value to be checked
        - studentList = list of students
    @return:
        - position, if it is valid
        - raises a RangeError, if the position is out of range
        - raises a ValueError, if the position is not convertible to integer
    '''
    position = int(position) #this may raise a ValueError
    if position < 0 or position >= len(studentList):
        raise RangeError('Position out of range')
        
    return position

def getValidNumber(number, numberType = 'I', low = 0, high = 10):
    '''
    Checks if a number is valid (integer (I) or float (F) between [low, high])
    @param:
        - number = value to be evaluated
        - numberType = character which represents the expected data type
             - 'I' = int
             - 'F' = float
        - low = lower bound of the range
        - high = higher bound of the range
    @return: 
        - number (integer), if the input was valid
        - raises an InputTypeError, if the range limits are not integers, or the expected data type is invalid
        - raises an RangeError, if the number is out of range
        - raises an RangeError, otherwise
    '''
    if not((isinstance(low, int) or isinstance(low, float)) and \
           (isinstance(high, int) or isinstance(high, float))):
        raise InputTypeError("Invalid number type for range limits")
        
    if low > high:
        raise RangeError("Invalid range limits")
        
    if numberType == 'I':
        number = int(number)
    elif numberType == 'F':
        number = float(number)
    else:
        raise InputTypeError("Invalid number type")
        
    if number < low or number > high:
        raise RangeError('Number out of range')
        
    return number

def getValidComparator(value):
    '''
    Checks if a value is a type of comparator (<,=,>)
    @param:
        - value = data to be evaluated
    @return: 
        - 0, if the value is '='
        - 1, if the value is '>'
        - 2, if the value is '<'
        - raises an InputTypeError, otherwise
    '''
    if value == "=":
        return 0
    if value == ">":
        return 1
    if value == "<":
        return 2
    raise InputTypeError("Invalid comparator")

def getValidProblem(value):
    '''
    Checks if value is a type of problem ("P1", "P2", "P3")
    @param:
        - value = string
    @return:
        - 1, if the problem is "P1"
        - 2, .. "P2"
        - 3, .. "P3"
        - raises an InputTypeError, otherwise
    '''
    if value == "P1":
        return 1
    if value == "P2":
        return 2
    if value == "P3":
        return 3
    
    raise InputTypeError("Invalid problem name")

