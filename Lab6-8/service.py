'''
    Contains everything related to action implementation
    All these methods should have valid input
'''

from domain import Movie, Client, Rental
from datetime import datetime

class Service(object):    
    def __init__(self, clients, movies):
        self.clientList = clients
        self.movieList = movies
        self.__rentID = 0
        
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
        
        return None
        
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
                [0] = index = integer (valid, guaranteed to be in the list)
                [1] = property = string (valid)
                [2] = newValue = string (valid)
                [3] = ID = integer (valid)
        @return:
            - None
        '''
        if argList[1] == "name":
            self.clientList[argList[0]] = Client(argList[3], argList[2])
    
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
        
        return None
    
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
                [0] = index = integer (valid, guaranteed to be in the list)
                [1] = property = string (valid)
                [2] = newValue = string (valid)
                [3] = ID = integer (valid)
        @return:
            - None
        '''            
        title = self.movieList[argList[0]].title
        description = self.movieList[argList[0]].description
        genre = self.movieList[argList[0]].genre
            
        if argList[1] == "title":
            self.movieList[argList[0]] = Movie(argList[3], argList[2], description, genre)
        elif argList[2] == "description":
            self.movieList[argList[0]] = Movie(argList[3], title, argList[2], genre)
        else:
            self.movieList[argList[0]] = Movie(argList[3], title, description, argList[2])

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
        Lets the user rent a movie (if available), starting from the current day
        @param:
            - argList = list of arguments, where:
                [0] = clientIndex = integer (valid)
                [1] = movieIndex = integer (valid)
                [2] = dueDate = date (valid)
                [3] = clientID = integer (valid)
                [4] = movieID = integer (valid)
        @return:
            - None
        '''
        clientIDX = argList[0]
        movieIDX = argList[1]

        self.__rentID += 1
        rentalObj = Rental(self.__rentID, argList[3], argList[4], datetime.today(), argList[2], None)
        self.clientList[clientIDX].addRental(rentalObj)
        self.movieList[movieIDX].isRented = True
                
    def returnMovie(self, argList):
        '''
        Lets the user return a movie 
        @param:
            - argList = list of arguments, where:
                [0] = clientID = integer (valid)
                [1] = rentalID = integer (valid)
                [2] = movieID = integer (valid)
        @return:
            - None
        '''
        clientIDX = argList[0]
        rentalIDX = argList[1]
        movieIDX = argList[2]
        
        self.clientList[clientIDX].returnMovie(rentalIDX)
        self.movieList[movieIDX].isRented = False

