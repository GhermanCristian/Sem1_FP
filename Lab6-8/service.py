'''
    Contains everything related to action implementation
    All these methods should have valid input
'''

from Domain.client import Client
from Domain.movie import Movie
from Domain.rental import Rental
from datetime import date
from customException import EmptyError
from undoController import UndoController

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
        
        self.rentalList.setIgnoreFlag(True)
        for idx in range(len(self.rentalList) - 1, -1, -1):
            if self.rentalList[idx].clientID == argList[0]:
                auxList.append(self.rentalList[idx])
                del self.rentalList[idx]
        self.rentalList.setIgnoreFlag(False)
        
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
        
        self.rentalList.setIgnoreFlag(True)
        for idx in range(len(self.rentalList) - 1, -1, -1):
            if self.rentalList[idx].movieID == argList[0]:
                auxList.append(self.rentalList[idx])
                del self.rentalList[idx]
        self.rentalList.setIgnoreFlag(False)
        
        movieCopy = self.movieList[argList[0]]
        del self.movieList[argList[0]]
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(1, [movieCopy, auxList], argList)
        
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
        elif argList[2] == "description":
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
                [2] = rentalIDX = integer (valid)
        @return:
            - None
        @raise:
            - EmptyError, if the IDs are not in their respective lists
        '''        
        self.movieList[argList[1]].isRented = False
        
        self.rentalList.setIgnoreFlag(True)
        self.rentalList[argList[2]].returnDate = date.today()
        self.rentalList.setIgnoreFlag(False)
        
        if self.__ignoreUndo == False:
            self.undoController.addAction(7, [argList[1], argList[2]], argList)
        
    def __reverseReturnMovie(self, argList):
        self.movieList[argList[0]].isRented = True
        
        self.rentalList.setIgnoreFlag(True)
        self.rentalList[argList[1]].returnDate = None
        self.rentalList.setIgnoreFlag(False)

    def searchClients(self, argList):
        '''
        Searches for a string in the clientList
        @param:
            - argList = list of arguments, where:
                [0] = subStr = string of integer (if ID) (valid)
                [1] = isID = boolean
        @return:
            - resultList = list of Clients
        @raise:
            - EmptyError, if the ID is not in the list
        '''
        self.clientList.setIgnoreFlag(True)
        
        #if the substring is an ID
        if argList[1] == True:
            for client in self.clientList:
                if client.ID == argList[0]:
                    self.clientList.setIgnoreFlag(False)
                    return [client, ]
            
            self.clientList.setIgnoreFlag(False)
            raise EmptyError("No client with this ID")
        
        argList[0] = argList[0].lower()
        resultList = []
        
        for client in self.clientList:
            if argList[0] in client.name.lower():
                resultList.append(client)      
                
        self.clientList.setIgnoreFlag(False)
        
        return resultList
    
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
        self.movieList.setIgnoreFlag(True)
        
        #if the substring is an ID
        if argList[1] == True:
            for movie in self.movieList:
                if movie.ID == argList[0]:
                    self.movieList.setIgnoreFlag(False)
                    return [movie, ]
            
            self.movieList.setIgnoreFlag(False)
            raise EmptyError("No movie with this ID")
        
        argList[0] = argList[0].lower()
        resultList = []
        
        for movie in self.movieList:
            if argList[0] in movie.title.lower() or argList[0] in movie.description.lower() or argList[0] in movie.genre.lower():
                resultList.append(movie)
                
        self.movieList.setIgnoreFlag(False)
        return resultList
    
    def __sortKeyMostActive(self, obj):
        return obj.daysRented
    
    def mostActive(self, argList):
        '''
        Creates a list of the most active clients / most rented movies
        @param:
            - argList = list of arguments, where
                [0] = either "client" or "movie"
        @return:
            - auxList = list of Clients or Movies
        '''
        self.rentalList.setIgnoreFlag(True)
        
        for rental in self.rentalList:
            if rental.returnDate == None: #hasn't been returned
                nrOfDays = (date.today() - rental.rentDate).days + 1
            else:
                nrOfDays = (rental.returnDate - rental.rentDate).days + 1
            
            if argList[0] == "movie":
                self.movieList[rental.movieID].daysRented += nrOfDays
            else:
                self.clientList[rental.clientID].daysRented += nrOfDays
                
        self.rentalList.setIgnoreFlag(False)
        
        if argList[0] == "movie":
            self.objList = self.movieList
        else:
            self.objList = self.clientList
        
        self.objList.setIgnoreFlag(True)
        
        auxList = []
        
        for obj in self.objList:
            auxList.append(obj)
        
        self.objList.setIgnoreFlag(False)
        
        auxList.sort(key = self.__sortKeyMostActive, reverse = True)
        return auxList
    
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
        
        self.rentalList.setIgnoreFlag(True)
        
        for rent in self.rentalList:
            if rent.dueDate < date.today() and rent.returnDate == None:
                lateRents.append(rent)
                
        self.rentalList.setIgnoreFlag(False)
        
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



