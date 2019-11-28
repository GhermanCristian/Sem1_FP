'''
'''
class Error(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return str(self.message)

class RangeError(Error):
    '''
    '''
    pass

class ArgError(Error):
    '''
    '''
    pass

class EmptyError(Error):
    '''
    '''
    pass

class MatchError(Error):
    '''
    '''
    pass

class DateError(Error):
    '''
    '''
    pass

class RentError(Error):
    '''
    '''
    pass

class UndoError(Error):
    '''
    '''
    pass

