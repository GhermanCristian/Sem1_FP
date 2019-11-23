'''
    Contains everything related to action implementation
    All these methods should have valid input
'''

from Domain.client import Client
from Domain.movie import Movie
from Domain.rental import Rental
from datetime import datetime
from customException import EmptyError

class Service(object):    
    def __init__(self, clients, movies, rentals):
        self.clientList = clients
        self.movieList = movies
        self.rentalList = rentals
        
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
        
    def removeClient(self, argList):
        '''
        Removes client by ID
        @param:
            - argList = list of arguments, where:
                [0] = index = integer (valid, guaranteed to be in the list)
        @return:
            - None
        '''
        del self.clientList[argList[0]]
    
    def updateClient(self, argList):
        '''
        Updates a client's properties
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid)
                [1] = property = string (valid)
                [2] = newValue = string (valid)
        @return:
            - None
        '''
        name = self.clientList[argList[0]].name
        
        if argList[1] == "name":
            self.clientList[argList[0]] = Client(argList[0], name)
    
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
    
    def removeMovie(self, argList):
        '''
        Removes movie by ID
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid)
        @return:
            - None
        '''
        del self.movieList[argList[0]]
    
    def updateMovie(self, argList):
        '''
        Updates a movie's properties
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid)
                [1] = property = string (valid)
                [2] = newValue = string (valid)
        @return:
            - None
        '''
        title = self.movieList[argList[0]].title
        description = self.movieList[argList[0]].description
        genre = self.movieList[argList[0]].genre
            
        if argList[1] == "title":
            self.movieList[argList[0]] = Movie(argList[0], argList[2], description, genre)
        elif argList[2] == "description":
            self.movieList[argList[0]] = Movie(argList[0], title, argList[2], genre)
        else:
            self.movieList[argList[0]] = Movie(argList[0], title, description, argList[2])

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
                [0] = clientID = integer (valid)
                [1] = movieID = integer (valid)
                [2] = rentDate = date (valid)
                [3] = dueDate = date (valid)
        @return:
            - None
        '''
        self.rentalList.increaseID()
        self.rentalList + Rental(self.rentalList.ID, argList[0], argList[1], argList[2], argList[3], None)
        self.movieList[argList[1]].isRented = True
                
    def returnMovie(self, argList):
        '''
        Lets the user return a movie 
        @param:
            - argList = list of arguments, where:
                [0] = clientID = integer (valid)
                [1] = movieID = integer (valid)
                [2] = rentalIDX = integer (valid)
        @return:
            - None
        '''
        self.movieList[argList[1]].isRented = False
        
        self.rentalList.setIgnoreFlag(True)
        nrOfDays = (datetime.today() - self.rentalList[argList[2]].rentDate).days + 1
        del self.rentalList[argList[2]]
        self.rentalList.setIgnoreFlag(False)
        
        self.movieList[argList[1]].daysRented += nrOfDays
        self.clientList[argList[0]].daysRented += nrOfDays

    def searchClients(self, argList):
        '''
        Searches for a string in the clientList
        @param:
            - argList = list of arguments, where:
                [0] = subStr = string (valid)
                [1] = isID = integer (valid)
        @return:
            - resultList = string
        '''
        self.clientList.setIgnoreFlag(True)
        
        if argList[1] == True:
            for client in self.clientList:
                if client.ID == argList[0]:
                    self.clientList.setIgnoreFlag(False)
                    return [str(client), ]
            
            self.clientList.setIgnoreFlag(False)
            raise EmptyError("No client with this ID")
        
        argList[0] = argList[0].lower()
        resultList = []
        
        for client in self.clientList:
            if argList[0] in client.name.lower():
                resultList.append(str(client))      
                
        self.clientList.setIgnoreFlag(False)
        return resultList
    
    def searchMovies(self, argList):
        '''
        Searches for a string in the movieList
        @param:
            - argList = list of arguments, where:
                [0] = subStr = string (valid)
                [1] = isID = integer (valid)
        @return:
            - resultList = list
        '''
        self.movieList.setIgnoreFlag(True)
        
        if argList[1] == True:
            for movie in self.movieList:
                if movie.ID == argList[0]:
                    self.movieList.setIgnoreFlag(False)
                    return [str(movie), ]
            
            self.movieList.setIgnoreFlag(False)
            raise EmptyError("No movie with this ID")
        
        argList[0] = argList[0].lower()
        resultList = []
        
        for movie in self.movieList:
            if argList[0] in movie.title.lower() or argList[0] in movie.description.lower() or argList[0] in movie.genre.lower():
                resultList.append(str(movie))
                
        self.movieList.setIgnoreFlag(False)
        return resultList

