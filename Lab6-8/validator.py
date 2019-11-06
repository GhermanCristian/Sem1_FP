'''
    Class of validator objects
'''
from customException import RangeError

class Validator(object):
    def validateIndex(self, index, low, high):
        '''
        Validates commandID
        @param:
            - index = string, current index
            - low = string, low part of the range
            - high = string, high part of the range
            
        @return:
            - integer value of index, if valid
            - None, otherwise
        @raise:
            - TypeError, if index, low or high are not integers
            - RangeError, if index is outside the range
        '''
        index = int(index)
        low = int(low)
        high = int(high)
        if low > high or low > index or high < index:
            raise RangeError("Element outside of range")
        
        return index