'''
 Module for the entity class (complex numbers)
'''

class ComplexNumber(object):
    '''
    Class for complex numbers
    '''
    
    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag
        
    @property
    def Real(self):
        return self.__real
        
    @property
    def Imag(self):
        return self.__imag

    def __eq__(self, com):
        return self.Real == com.Real and self.Imag == com.Imag    