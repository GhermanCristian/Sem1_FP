'''
    Class of validators
'''
from customException import RangeError, ArgError, EmptyError, MatchError, DateError,\
    RentError
from datetime import datetime

class Validator(object):
    def __init__(self, clientList, movieList):
        self.clients = clientList
        self.movies = movieList
    
    def validateIndex(self, index, low, high):
        '''
        Validates index
        @param:
            - index = string(?), current index
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
    
    def __findClientByID(self, ID):
        '''
        Finds a client in clientList
        @param:
            - ID = integer (valid)
        @return:
            - index of the client in clientList, if it exists
            - None, otherwise
        '''
        for idx in range(len(self.clients)):
            if self.clients[idx].ID == ID:
                return idx
            
        raise EmptyError("Cannot find a client with that ID. (Maybe it has been deleted ?)")
    
    def __findMovieByID(self, ID):
        '''
        Finds a movie in movieList
        @param:
            - ID = integer (valid)
        @return:
            - index of the movie in movieList, if it exists
            - None, otherwise
        '''
        for idx in range(len(self.movies)):
            if self.movies[idx].ID == ID:
                return idx
            
        raise EmptyError("Cannot find a movie with that ID. (Maybe it has been deleted ?)")    
    
    def canRent(self, idx):
        '''
        Checks if a client at index idx can rent a movie
        @param:
        @return:
        @raise:
        '''
        crtDate = datetime.today()
        for rental in self.clients[idx].rentals:
            if rental.dueDate < crtDate:
                print (rental.dueDate)
                print (crtDate)
                raise RentError("Client cannot rent movies - needs to return overdue movies") 

    def hasRented(self, clientIDX, movieID):
        '''
        Checks if a client has rented a movie
        @param:
            - movieID = integer, valid
        @return:
            - i = integer = index of the rental containing that movie in the client's rentalList
        '''    
        for i in range(len(self.clients[clientIDX].rentals)):
            if self.clients[clientIDX].rentals[i].movieID == movieID:
                return i
            
        raise RentError("This client has not rented this movie (or has already returned it)")
    
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
            - EmptyError, if the ID is not in the list
        '''
        l = len(argList)
        if l is not 1:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)
        argList[0] = self.__findClientByID(argList[0])
        
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
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)
        #argList[3] will be the client's ID
        argList.append(argList[0])
        #argList[0] will be the client's index in clientList
        argList[0] = self.__findClientByID(argList[0])
        
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
        argList[0] = self.validateIndex(argList[0], 1, self.movies.ID)
        argList[0] = self.__findMovieByID(argList[0])
        
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
        
        argList[0] = self.validateIndex(argList[0], 1, self.movies.ID)
        argList.append(argList[0])
        argList[0] = self.__findMovieByID(argList[0])
        
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
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)
        argList.append(argList[0])
        argList[0] = self.__findClientByID(argList[0])

        #check that the client can rent a movie
        self.canRent(argList[0])
        
        argList[1] = self.validateIndex(argList[1], 1, self.movies.ID)
        argList.append(argList[1])
        argList[1] = self.__findMovieByID(argList[1])
        
        #check tht the movie can be rented
        if self.movies[argList[1]].isRented == True:
            raise RentError("Movie is already rented by someone")
        
        argList[2] = self.validateDate(argList[2])
        if argList[2] < datetime.today():
            raise DateError("Due date cannot be in the past")
        
        return argList
        
    def valReturnMovie(self, argList):
        '''
        Validates input for returnMovie
        @param:
            - argList = list of arguments, where:
                [0] = clientID = string
                [1] = movieID = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - TypeError, if any of the IDs are not integers
            - RangeError, if any of the IDs are out of range
        '''
        l = len(argList)
        
        if l is not 2:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)
        argList[0] = self.__findClientByID(argList[0])
        
        argList[1] = self.validateIndex(argList[1], 1, self.movies.ID)
        argList.append(self.__findMovieByID(argList[1]))
        
        #check that the client has rented this movie
        argList[1] = self.hasRented(argList[0], argList[1])
        
        if self.movies[argList[2]].isRented == False:
            raise RentError("This movie is not rented by anyone")
        
        return argList

'''
x = Validator(1,2)
print(x.validateDate("15-12-2020"))
y = datetime(2019, 12, 15)
print (x.validateDate("15-12-2020") > y)
'''

