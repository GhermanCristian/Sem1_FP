from customExceptions import RangeError, InputTypeError

def isValidPosition(position, studentList):
    '''
    Checks if 'position' is valid within the current studentList
    @param:
        - position = value to be checked
        - studentList = list of students
    @return:
        - position, if it is valid
        - -1, otherwise
    '''
    try:
        position = int(position)
        if position < 0 or position >= len(studentList):
            raise RangeError('Position out of range')
        
        return position
        
    except ValueError:
        print ("Invalid value type")
        return -1
    
    except RangeError:
        return -1

def isValidNumber(number, numberType = 'I', low = 0, high = 10):
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
        - -1, otherwise
    '''
    try:
        if not((isinstance(low, int) or isinstance(low, float)) and \
               (isinstance(high, int) or isinstance(high, float))):
            raise InputTypeError("Invalid number type for range limits")
        
        if low > high:
            raise ArithmeticError
        
        if numberType == 'I':
            number = int(number)
        elif numberType == 'F':
            number = float(number)
        else:
            raise InputTypeError("Invalid number type")
        
        if number < low or number > high:
            raise RangeError('Number out of range')
        
        return number
    
    except ValueError:
        print ("Invalid value type")
        return -1
    except InputTypeError:
        return -1
    except RangeError:
        return -1
    except ArithmeticError:
        print ("Invalid range limits")
        return -1

def isValidComparator(value):
    '''
    Checks if a value is a type of comparator (<,=,>)
    @param:
        - value = data to be evaluated
    @return: 
        - 0, if the value is '='
        - 1, if the value is '>'
        - 2, if the value is '<'
        - -1, otherwise
    '''
    try:
        if value == "=":
            return 0
        if value == ">":
            return 1
        if value == "<":
            return 2
        raise InputTypeError("Invalid comparator")
    
    except InputTypeError:
        return -1

def isValidKeyword(expectedKeyword, actualKeyword):
    '''
    Checks if expectedKeyword is equal to actualKeyword
    @param:
        - expectedKeyword = string
        - actualKeyword = string
    @return:
        - a boolean value representing the truthhood of the expression
    '''
    
    try: 
        if not(isinstance(expectedKeyword, str) and isinstance(actualKeyword, str)):
            raise InputTypeError("Invalid type: str required")
        if expectedKeyword == actualKeyword:
            return True
        raise InputTypeError("Missing keyword: " + expectedKeyword)
    
    except InputTypeError:
        return False

def isValidProblem(value):
    '''
    Checks if value is a type of problem ("P1", "P2", "P3")
    @param:
        - value = string
    @return:
        - 1, if the problem is "P1"
        - 2, .. "P2"
        - 3, .. "P3"
        - -1, otherwise
    '''
    try:
        if value == "P1":
            return 1
        if value == "P2":
            return 2
        if value == "P3":
            return 3
        raise InputTypeError("Invalid problem name")
    
    except InputTypeError:
        return -1

