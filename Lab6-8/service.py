'''
    Contains everything related to action implementation
    All these methods should have valid input
'''

from domain import Movie, Client

class Service(object):    
    def __init__(self):
        self.clientList = []
        self.__clientID = 0
        self.movieList = []
        self.__movieID = 0
        
    def countClients(self):
        return self.__clientID

    def countMovies(self):
        return self.__movieID
    
    def __findClientByID(self, ID):
        '''
        Finds a client in clientList
        @param:
            - ID = integer (valid)
        @return:
            - index of the client in clientList, if it exists
            - None, otherwise
        '''
        for idx in range(len(self.clientList)):
            if self.clientList[idx].ID == ID:
                return idx
        return None
    
    def __findMovieByID(self, ID):
        '''
        Finds a movie in movieList
        @param:
            - ID = integer (valid)
        @return:
            - index of the movie in movieList, if it exists
            - None, otherwise
        '''
        for idx in range(len(self.movieList)):
            if self.movieList[idx].ID == ID:
                return idx
        return None
        
    def addClient(self, argList):
        '''
        Adds client to clientList
        @param:
            - argList = list of arguments, where:
                [0] = name = string (valid), representing the client's name
        @return:
            - None
        '''
        self.__clientID += 1
        self.clientList.append(Client(self.__clientID, argList[0]))
        
        return None
        
    def removeClient(self, argList):
        '''
        Removes client by ID
        @param:
            - argList = list of arguments, where:
                [0] = ID = integer (valid)
        @return:
            - None
        '''
        idx = self.__findClientByID(argList[0])
        if idx is not None:
            self.clientList.pop(idx)
    
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
        idx = self.__findClientByID(argList[0])
        if idx is not None:
            '''prop = {
                    "name": self.clientList[idx].name
                   }
            prop[argList[1]] = argList[2]'''
            if argList[1] == "name":
                
                self.clientList[idx].name = argList[2]
    
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
        self.__movieID += 1
        self.movieList.append(Movie(self.__movieID, argList[0], argList[1], argList[2]))
        
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
        idx = self.__findMovieByID(argList[0])
        if idx is not None:
            self.movieList.pop(idx)
    
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
        idx = self.__findMovieByID(argList[0])
        if idx is not None:
            prop = {
                    "title": self.movieList[idx].title,
                    "description": self.movieList[idx].description,
                    "genre": self.movieList[idx].genre
                   }
            prop[argList[1]] = argList[2]

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

