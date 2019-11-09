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
        for idx in range(len(self.clientList)):
            if self.clientList[idx].ID == argList[0]:
                self.clientList.pop(idx)
                return None
    
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
        for idx in range(len(self.movieList)):
            if self.movieList[idx].ID == argList[0]:
                self.movieList.pop(idx)
                return None
    


    


