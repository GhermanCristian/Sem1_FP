'''
User-defined errors
'''

class Error(Exception):
    '''
    Base class for user-defined exceptions
    '''
    def __init__(self, message):
        print (str(message))

class RangeError(Error):
    '''
    User-defined error; occurs
    - when an integer / floating point value is not inside a specified range
    - when the limits of a range [a, b] do not satisfy that a <= b
    '''
    pass

class InputTypeError(Error):
    '''
    User-defined error; occurs when the type of the input value is invalid
    '''
    pass
        
class ParamError(Error):
    '''
    User-defined error; occurs when a function's parameters are invalid
    (e.g. incorrect number of parameters)
    '''
    pass

class EmptyPositionError(Error):
    '''
    User-defined error; occurs when trying to do an operation on an empty position
    '''
    pass
