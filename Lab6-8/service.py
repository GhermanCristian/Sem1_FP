'''
    Contains everything related to action implementation
'''

from domain import Movie, Client

class Service(object):    
    def __init__(self):
        self.clientList = []
        self.movieList = []
        self.commandList = [
            self.addClient, 
            self.removeClient,
            self.updateClient,
            self.addMovie,
            self.removeMovie,
            self.updateMovie,
            
        ]
        
    def addClient(self, name):
        '''
        Adds client to clientList
        *i should check that it doesn't already exist ?
        @param:
            - name = string (valid), representing the client's name
        @return:
            - None
        '''
        ID = len(self.clientList)
        self.clientList.append(Client(ID, name))
        
    def removeClient(self, ID):
        '''
        Removes client with ID
        @param:
            - ID = integer, should be inside the list
        @return:
            - None
        '''
        self.clientList.pop(ID)
        
    def updateClient(self, ID, name):
        self.clientList[ID].updateClient()
    
    def addMovie(self, name, description, genre):
        '''
        '''
        ID = len(self.movieList)
        self.movieList.append(Movie(ID, name, description, genre))
    
    def removeMovie(self, ID):
        '''
        '''
        self.movieList.pop(ID)
    
    def updateMovie(self, ID, title, description, genre):
        self.movieList[ID].updateMovie(title, description, genre)



    


