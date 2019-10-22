class Error(Exception):
    '''
    Base class for user-defined exceptions
    '''
    def __init__(self, message):
        print (str(message))

class RangeError(Error):
    '''
    User-defined error; occurs when an integer / floating point value is not inside a specified range
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
