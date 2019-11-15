'''
    Class of validators
'''
from customException import RangeError, ArgError, EmptyError, MatchError
from datetime import datetime

class Validator(object):
    def __init__(self, countClients, countMovies):
        self.clients = countClients
        self.movies = countMovies
    
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
    
    def validateDate(self, dateInput):
        '''
        Validates a date
        @param:
            - dateInput = string, represents a date, in the form "day-month-year", all numbers
        @return:
            - dateInput as a Datetime type, if valid
        @raise:
            - EmptyError, if dateInput is an empty string
            - ValueError, if dateInput is not a valid date
        '''
        l = len(dateInput)
        
        if l == 0:
            raise EmptyError("Date cannot be empty")
        
        dateInput = datetime.strptime(dateInput, "%d-%m-%Y")
        
        return dateInput
        
    
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
            - EmptyError, if the name is an empty string
        '''
        l = len(argList)
        if l is not 1:
            raise ArgError("Invalid number of arguments")
        if len(argList[0]) < 3:
            raise EmptyError("Name is too short")
        
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
    
    def valUpdateClient(self, argList):
        '''
        Validates input for updateClient
        @param:
            - argList = list of arguments, where:
                [0] = ID = string
                [1] = property = string
                [2] = newValue = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - TypeError, if ID is not an integer
            - RangeError, if ID is out of range
            - EmptyError, if the property or the new value are empty strings
        '''
        l = len(argList)
        if l is not 3:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients)
        
        if len(argList[1]) == 0:
            raise EmptyError("Property cannot be empty")
        if argList[1] not in ["name",]:
            raise MatchError("Input cannot match any property")  
        
        if len(argList[2]) < 3:
            raise EmptyError("Name is too short")
        
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
            raise ArgError("Invalid number of arguments")
        if len(argList[0]) < 3:
            raise EmptyError("Title is too short")
        if len(argList[1]) < 3:
            raise EmptyError("Description is too short")
        if len(argList[2]) < 3:
            raise EmptyError("Genre is too short")
        
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

    def valUpdateMovie(self, argList):
        '''
        Validates input for updateMovie
        @param:
            - argList = list of arguments, where:
                [0] = ID = string
                [1] = property = string
                [2] = newValue = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - TypeError, if ID is not an integer
            - RangeError, if ID is out of range
            - MatchError, if the input doesn't match any properties
            - EmptyError, if the property or the new value are empty strings
        '''
        l = len(argList)
        if l is not 3:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.movies)
        
        if len(argList[1]) == 0:
            raise EmptyError("Property cannot be empty")
        if argList[1] not in ["title", "description", "genre"]:
            raise MatchError("Input doesn't match any property")  
        
        if len(argList[2]) < 3:
            raise EmptyError("New value is too short") 
        
        return argList 
    
    def valPrintList(self, argList):
        '''
        Validates input for getList
        @param:
            - argList = list of arguments, where:
                [0] = type of list = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - MatchError, if the input doesn't match either "client" or "movie"
            - EmptyError, if the given input is an empty string
        '''
        l = len(argList)
        if l is not 1:
            raise ArgError("Invalid number of arguments")
        
        if len(argList[0]) == 0:
            raise EmptyError("Input cannot be empty")
        
        if argList[0] not in ["client", "movie"]:
            raise MatchError("Input doesn't match any type")
        
        return argList

    def valRentMovie(self, argList):
        '''
        Validates input for rentMovie
        @param:
            - argList = list of arguments, where:
                [0] = clientID = string
                [1] = movieID = string
                [2] = dueDate = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - TypeError, if any of the IDs are not integers
            - RangeError, if any of the IDs are out of range
        '''
        l = len(argList)
        
        if l is not 3:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients)
        argList[1] = self.validateIndex(argList[1], 1, self.movies)
        argList[2] = self.validateDate(argList[2])
        
        return argList
        
    def valReturnMovie(self, argList):
        '''
        Validates input for returnMovie
        @param:
            - argList = list of arguments, where:
        @return:
        @raise:
        '''
        
        return argList

'''
x = Validator(1,2)
print(x.validateDate("15-12-2020"))
y = datetime(2019, 12, 15)
print (x.validateDate("15-12-2020") > y)
'''

