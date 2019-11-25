'''
    Class of validators
'''
from customException import RangeError, ArgError, EmptyError, MatchError, DateError, RentError
from datetime import datetime

class Validator(object):
    def __init__(self, clientList, movieList, rentalList):
        self.clients = clientList
        self.movies = movieList
        self.rentals = rentalList
    
    def validateIndex(self, index, low, high):
        '''
        Validates index
        @param:
            - index - can be either string or integer = current index
            - low = can be either string or integer = low part of the range
            - high = can be either string or integer = high part of the range
        @return:
            - integer value of index, if valid
        @raise:
            - ValueError, if index, low or high are not integers
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
            - dateInput = string, represents a date, in the form "DD-MM-YYYY", all numbers
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
    
    def canRent(self, ID):
        '''
        Checks if a client, determined by its ID, can rent a movie
        @param:
            - ID = integer = client's ID
        @return:
            - None
        @raise:
            - RentError, if the client cannot rent movies
        '''
        self.rentals.setIgnoreFlag(True)
        
        for idx in range(len(self.rentals)):
            if self.rentals[idx].clientID == ID and datetime.today() > self.rentals[idx].dueDate:
                self.rentals.setIgnoreFlag(False)
                raise RentError("Client cannot rent movies - it needs to return late ones")
            
        self.rentals.setIgnoreFlag(False)

    def hasRented(self, clientID, movieID):
        '''
        Checks if a client has rented a movie
        @param:
            - clientID = integer
            - movieID = integer
        @return:
            - idx = index of client which has rented the movie (if it exists)
        @raise:
            - RentError, if the client has not rented the movie
        '''    
        self.rentals.setIgnoreFlag(True)
        
        for idx in range(len(self.rentals)):
            if self.rentals[idx].clientID == clientID and self.rentals[idx].movieID == movieID:
                self.rentals.setIgnoreFlag(False)
                return idx
        
        self.rentals.setIgnoreFlag(False)
        raise RentError("This client has not rented this movie (maybe it has already returned it)")
    
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
            - EmptyError, if the name is too short
        '''
        if len(argList) is not 1:
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
            - ValueError, if ID is not an integer
            - RangeError, if ID is out of range
        '''
        if len(argList) is not 1:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)
        
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
            - ValueError, if ID is not an integer
            - RangeError, if ID is out of range
            - EmptyError, if the new value is too short
            - MatchError, if the input doesn't match any properties
        '''
        if len(argList) is not 3:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)

        if argList[1] not in ["name",]:
            raise MatchError("Input cannot match any property")  
        
        if len(argList[2]) < 3:
            raise EmptyError("New name is too short")
        
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
            - EmptyError, if one the properties is too short
        '''
        if len(argList) is not 3:
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
            - ValueError, if ID is not an integer
            - RangeError, if ID is out of range
        '''
        if len(argList) is not 1:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.movies.ID)
        
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
            - ValueError, if ID is not an integer
            - RangeError, if ID is out of range
            - MatchError, if the input doesn't match any properties
            - EmptyError, if the new value is too short
        '''
        if len(argList) is not 3:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.movies.ID)
        
        if argList[1] not in ["title", "description", "genre"]:
            raise MatchError("Input doesn't match any property")  
        
        if len(argList[2]) < 3:
            raise EmptyError("New value is too short") 
        
        return argList 
    
    def valSeparator(self, argList):
        '''
        Validates input for getList, mostActive, lateRental
        @param:
            - argList = list of arguments, where:
                [0] = type of list = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - MatchError, if the input doesn't match either "client" or "movie"
        '''
        if len(argList) is not 1:
            raise ArgError("Invalid number of arguments")
        
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
                [2] = rentDate = string
                [3] = dueDate = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - ValueError, if any of the IDs are not integers or if the dates are invalid
            - RangeError, if any of the IDs are out of range
            - RentError, if the client cannot rent any movies or if the movie is already rented
            - DateError, if the due date is before the rent date
        '''
        if len(argList) is not 4:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)

        #check that the client can rent a movie
        self.canRent(argList[0])
        
        argList[1] = self.validateIndex(argList[1], 1, self.movies.ID)
        
        #check that the movie can be rented
        if self.movies[argList[1]].isRented == True:
            raise RentError("Movie is already rented by someone")
        
        argList[2] = self.validateDate(argList[2])
        argList[3] = self.validateDate(argList[3])
        
        if argList[2] > argList[3]:
            raise DateError("Due date cannot be before the rent date")
        
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
            - ValueError, if any of the IDs are not integers
            - RangeError, if any of the IDs are out of range
            - RentError, if the client has not rented the movie or if the movie is not rented by anyone
        '''
        if len(argList) is not 2:
            raise ArgError("Invalid number of arguments")
        
        argList[0] = self.validateIndex(argList[0], 1, self.clients.ID)
        argList[1] = self.validateIndex(argList[1], 1, self.movies.ID)
        
        #check that the client has rented this movie
        argList.append(self.hasRented(argList[0], argList[1]))
        
        if self.movies[argList[1]].isRented == False:
            raise RentError("This movie is not rented by anyone")
        
        return argList

    def valSearch(self, argList):
        '''
        Validates input for searchClient and searchMovie
        @param:
            - argList = list of arguments, where:
                [0] = subStr = string
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
            - ValueError, if any of the IDs are not integers
            - RangeError, if any of the IDs are out of range
            - EmptyError, if the substring is too short
        '''
        if len(argList) is not 1:
            raise ArgError("Invalid number of arguments")
        
        #if the subStr is not an integer => it is not an ID => it is one of the other properties
        aux = ""
        try:
            aux = self.validateIndex(argList[0], 1, self.clients.ID)
        except:
            pass
        
        #aux is an integer => is an ID => we set the value of isID to True
        if isinstance(aux, int):
            argList[0] = aux
            argList.append(True)
            return argList
        
        if len(argList[0]) < 3:
            raise EmptyError("Value is too short")
        
        #aux is not an integer => isID will be False
        argList.append(False)
        return argList
    
    def valLateRentals(self, argList):
        '''
        Validates input for lateRentals
        @param:
            - argList = list of arguments, empty
        @return:
            - argList, if valid
        @raise:
            - ArgError, if the argList is invalid
        '''
        if len(argList) is not 0:
            raise ArgError("Invalid number of arguments")
        
        return argList
    
    def valUndo(self, argList):
        pass
    
    def valRedo(self, argList):
        pass



