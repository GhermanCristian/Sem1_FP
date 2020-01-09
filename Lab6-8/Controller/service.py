'''
    Contains everything related to action implementation
    All these methods should have valid input
'''

from Domain.client import Client
from Domain.movie import Movie
from Domain.rental import Rental
from datetime import date
from Controller.customException import EmptyError
from Controller.undoController import UndoController

class Service(object):
    '''
    Class for the 
    Fields:
        Public:
            - None
        Private:
            - None
    Methods:
        Public:
            - None
        Private:
            - None
    Properties:
        - None
    Setters:
        - None
    '''    
    def __init__(self, clients, movies, rentals):
        self.clientList = clients
        self.movieList = movies
        self.rentalList = rentals
        self.undoController = UndoController()
        
        self.__ignoreUndo = False
        
        #this is used for the "redo" functionality (the __ignoreUndo flag will be set to True so that calling these functions
        #does not add new commands to the undoController actionList (cascade effect)
        self.__normalActionList = [
            self.addClient,
            self.removeClient,
            self.updateClient,
            self.addMovie,
            self.removeMovie,
            self.updateMovie,
            self.rentMovie,
            self.returnMovie
        ]
        
        #this is used for the "undo" functionality
        self.__reverseActionList = [
            self.__reverseAddClient,
            self.__reverseRemoveClient,
            self.__reverseUpdateClient,
            self.__reverseAddMovie,
            self.__reverseRemoveMovie,
            self.__reverseUpdateMovie,
            self.__reverseRentMovie,
            self.__reverseReturnMovie
        ]
        
    def addClient(self, argList):
        '''
        Adds a client to clientList
        @param:
            - argList = list of arguments, where:
                [0] = name = string (valid), representing the client's name
        @return:
            - None
        '''
        self.clientList.increaseID()
        self.clientList + Client(self.clientList.ID, argList[0])
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(0, [], argList)
        
    def __reverseAddClient(self, argList):
        del self.clientList[self.clientList.ID]
        self.clientList.decreaseID()
        
    def removeClient(self, argList):
        '''
        Removes client by ID
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid, not guaranteed to be in the list)
        @return:
            - None
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        #this will contain all the rentals of this client
        auxList = []

        for rent in self.rentalList:
            if rent.clientID == argList[0]:
                auxList.append(rent)
                
        #I cannot delete directly in the for loop above this, hence why I am using this
        for rent in auxList:
            del self.rentalList[rent.ID]
        
        clientCopy = self.clientList[argList[0]]
        del self.clientList[argList[0]]
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(1, [clientCopy, auxList], argList)
        
    def __reverseRemoveClient(self, argList):
        self.clientList + argList[0]
        for rental in argList[1]:
            self.rentalList + rental
    
    def updateClient(self, argList):
        '''
        Updates a client's properties
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid, not guaranteed to be in the list)
                [1] = property = string (valid)
                [2] = newValue = string (valid)
        @return:
            - None
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        clientCopy = self.clientList[argList[0]]

        if argList[1] == "name":
            self.clientList[argList[0]] = Client(argList[0], argList[2])  
            
        if self.__ignoreUndo == False:
            self.undoController.addAction(2, [argList[0], clientCopy], argList)
            
    def __reverseUpdateClient(self, argList):
        self.clientList[argList[0]] = argList[1]
    
    def addMovie(self, argList):
        '''
        Adds movie to movieList
        @param:
            - argList = list of arguments, where:
                [0] = title = string (valid), representing the movie's title
                [1] = description = string (valid), the movie's description
                [2] = genre = string (valid), the movie's genre
        @return:
            - None
        '''
        self.movieList.increaseID()
        self.movieList + Movie(self.movieList.ID, argList[0], argList[1], argList[2])
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(3, [], argList)
        
    def __reverseAddMovie(self, argList):
        del self.movieList[self.movieList.ID]
        self.movieList.decreaseID()
    
    def removeMovie(self, argList):
        '''
        Removes movie by ID
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid, not guaranteed to be in the list)
        @return:
            - None
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        #this will contain all the rentals of this movie
        auxList = []
        
        for rent in self.rentalList:
            if rent.movieID == argList[0]:
                auxList.append(rent)
                
        for rent in auxList:
            del self.rentalList[rent.ID]
        
        movieCopy = self.movieList[argList[0]]
        del self.movieList[argList[0]]
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(4, [movieCopy, auxList], argList)
        
    def __reverseRemoveMovie(self, argList):
        self.movieList + argList[0]
        for rental in argList[1]:
            self.rentalList + rental
    
    def updateMovie(self, argList):
        '''
        Updates a movie's properties
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid, not guaranteed to be in the list)
                [1] = property = string (valid)
                [2] = newValue = string (valid)
        @return:
            - None
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        movieCopy = self.movieList[argList[0]]
        
        title = self.movieList[argList[0]].title
        description = self.movieList[argList[0]].description
        genre = self.movieList[argList[0]].genre
            
        if argList[1] == "title":
            self.movieList[argList[0]] = Movie(argList[0], argList[2], description, genre)
        elif argList[1] == "description":
            self.movieList[argList[0]] = Movie(argList[0], title, argList[2], genre)
        else:
            self.movieList[argList[0]] = Movie(argList[0], title, description, argList[2])
            
        if self.__ignoreUndo == False:
            self.undoController.addAction(5, [argList[0], movieCopy], argList)

    def __reverseUpdateMovie(self, argList):
        self.movieList[argList[0]] = argList[1]
    
    def getList(self, argList):
        '''
        Returns either clientList or movieList
        @param:
            - argList = list of arguments, where:
                [0] = type of list = string (valid)
        @return:
            - self.clientList, if type of list = "client"
            - self.movieList, otherwise
        '''
        if argList[0] == "client":
            return self.clientList
        if argList[0] == "rental":
            return self.rentalList
        return self.movieList

    def rentMovie(self, argList):
        '''
        Lets the user rent a movie (if available), starting from a given day
        @param:
            - argList = list of arguments, where:
                [0] = clientID = integer (valid, not guaranteed to be in the list)
                [1] = movieID = integer (valid, not guaranteed to be in the list)
                [2] = rentDate = date (valid)
                [3] = dueDate = date (valid)
        @return:
            - None
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        self.rentalList.increaseID()
        self.rentalList + Rental(self.rentalList.ID, argList[0], argList[1], argList[2], argList[3], None)
        self.movieList[argList[1]].isRented = True
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(6, [argList[1]], argList)
            
    def __reverseRentMovie(self, argList):
        self.movieList[argList[0]].isRented = False
        del self.rentalList[self.rentalList.ID]
        self.rentalList.decreaseID()
                
    def returnMovie(self, argList):
        '''
        Lets the user return a movie 
        @param:
            - argList = list of arguments, where:
                [0] = clientID = integer (valid, not guaranteed to be in the list)
                [1] = movieID = integer (valid, not guaranteed to be in the list)
                [2] = rentalID = integer (valid)
        @return:
            - None
        @raise:
            - EmptyError, if the IDs are not in their respective lists
        '''        
        self.movieList[argList[1]].isRented = False
        self.rentalList[argList[2]].returnDate = date.today()
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(7, [argList[1], argList[2]], argList)
        
    def __reverseReturnMovie(self, argList):
        self.movieList[argList[0]].isRented = True
        self.rentalList[argList[1]].returnDate = None

    def __clientFilter(self, isID, val, client):
        '''
        '''
        if isID == True:
            return client.ID == val
        
        val = val.lower()
        return val in client.name.lower()

    def searchClients(self, argList):
        '''
        Searches for a string in the clientList
        @param:
            - argList = list of arguments, where:
                [0] = subStr = string or integer (if ID) (valid)
                [1] = isID = boolean
        @return:
            - resultList = list of Clients
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        return self.clientList.filter(self.__clientFilter, argList[0], argList[1])
    
    def __movieFilter(self, isID, val, movie):
        '''
        '''
        if isID == True:
            return movie.ID == val
        
        val = val.lower()
        return val in movie.title.lower() or val in movie.description.lower() or val in movie.genre.lower()
    
    def searchMovies(self, argList):
        '''
        Searches for a string in the movieList
        @param:
            - argList = list of arguments, where:
                [0] = subStr = string or integer (if ID) (valid)
                [1] = isID = boolean
        @return:
            - resultList = list of Movies
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        return self.movieList.filter(self.__movieFilter, argList[0], argList[1])
    
    def __cmpMostActive(self, obj1, obj2):
        return obj1.daysRented > obj2.daysRented
    
    def mostActive(self, argList):
        '''
        Creates a list of the most active clients / most rented movies
        @param:
            - argList = list of arguments, where
                [0] = either "client" or "movie"
        @return:
            - auxList = list of Clients or Movies
        '''
        for rental in self.rentalList:
            if rental.returnDate == None: #hasn't been returned
                nrOfDays = (date.today() - rental.rentDate).days + 1
            else:
                nrOfDays = (rental.returnDate - rental.rentDate).days + 1
            
            if argList[0] == "movie":
                self.movieList[rental.movieID].daysRented += nrOfDays
            else:
                self.clientList[rental.clientID].daysRented += nrOfDays
        
        if argList[0] == "movie":
            return self.movieList.sort(self.__cmpMostActive)
        return self.clientList.sort(self.__cmpMostActive)
    
    def __sortKeyLateRentals(self, rental):
        return rental.dueDate
    
    def lateRentals(self, argList):
        '''
        Creates a list of late rentals
        @param:
            - argList = list of arguments = empty
        @return:
            - lateRents = list of strings
        '''
        lateRents = []
        
        for rent in self.rentalList:
            if rent.dueDate < date.today() and rent.returnDate == None:
                lateRents.append(rent)
        
        lateRents.sort(key = self.__sortKeyLateRentals)

        return lateRents
    
    def undo(self, argList):
        '''
        Undoes the last performed operation
        @param:
            - argList = list of arguments = empty
        @return:
            - None
        '''
        action = self.undoController.undo()
        actionID = action[0]
        revArgList = action[1]
        self.__reverseActionList[actionID](revArgList)
    
    def redo(self, argList):
        '''
        Redoes the last performed operation
        @param:
            - argList = list of arguments = empty
        @return:
            - None
        '''
        action = self.undoController.redo()
        actionID = action[0]
        normArgList = action[2]
        
        #when undo is ignored, the functions called by redo (those in __normalActionList) will no longer append any
        #commands to the undoController actionList
        self.__ignoreUndo = True
        self.__normalActionList[actionID](normArgList)
        self.__ignoreUndo = False

