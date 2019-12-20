class Error(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return str(self.message)
    
class EmptyError(Error):
    '''
    '''
    pass

class RangeError(Error):
    '''
    '''
    pass