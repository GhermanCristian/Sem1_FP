'''
    Class of validators
'''
from customException import RangeError, ArgError, EmptyError

class Validator(object):
    def __init__(self, countClients, countMovies):
        self.clients = countClients
        self.movies = countMovies
        print ("created new validator, with movies = " + str(self.movies))
    
    def validateIndex(self, index, low, high):
        '''
        Validates index
        @param:
            - index = string, current index
            - low = string, low part of the range
            - high = string, high part of the range
        @return:
            - integer value of index, if valid
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
    
    def valAddClient(self, argList):
        '''
        Validates input for addClient
        @param:
            - argList = list of arguments, where:
                [0] = name = string, representing the client's name
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
        '''
        l = len(argList)
        if l is not 1:
            raise ArgError("Invalid number of arguments")
        if len(argList[0]) == 0:
            raise EmptyError("Name cannot be empty")
        
        return argList
    
    def valRemClient(self, argList):
        '''
        Validates input for removeClient
        @param:
            - argList = list of arguments, where:
                [0] = ID = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - TypeError, if ID is not an integer
            - RangeError, if ID is out of range
        '''
        l = len(argList)
        if l is not 1:
            raise ArgError("Invalid number of arguments")
        argList[0] = self.validateIndex(argList[0], 1, self.clients)
        
        return argList
         
    def valAddMovie(self, argList):
        '''
        Validates input for addMovie
        @param:
            - argList = list of arguments, where:
                [0] = title = string, representing the movie's title
                [1] = description = string, the movie's description
                [2] = genre = string, the movie's genre
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
        '''
        l = len(argList)
        if l is not 3:
            print("hello wtf")
            raise ArgError("Invalid number of arguments")
        if len(argList[0]) == 0:
            raise EmptyError("Title cannot be empty")
        if len(argList[1]) == 0:
            raise EmptyError("Description cannot be empty")
        if len(argList[2]) == 0:
            raise EmptyError("Genre cannot be empty")
        
        return argList

    def valRemMovie(self, argList):
        '''
        Validates input for removeMovie
        @param:
            - argList = list of arguments, where:
                [0] = ID = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - TypeError, if ID is not an integer
            - RangeError, if ID is out of range
        '''
        l = len(argList)
        if l is not 1:
            raise ArgError("Invalid number of arguments")
        argList[0] = self.validateIndex(argList[0], 1, self.movies)
        
        return argList

