from constants import CLIENT_FILE, MOVIE_FILE, CLIENT_COUNT, MOVIE_COUNT
import os
import random
from domain import Client, Movie
from clientRepo import ClientRepo
from movieRepo import MovieRepo

'''
I will assume that all the input is valid, and that there's no need to verify it
'''
class ClientListGenerator(object):
    def __init__(self):
        self.count = CLIENT_COUNT
    
    def __getClients(self):
        '''
        Creates a clientList with the data from CLIENT_FILE
        @param:
            - None
        @return:
             - clientList = list of tuples (title, description, genre)
        '''
        clientList = []
        
        filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), CLIENT_FILE)
        clientFile = open(filePath, "r")
    
        while True:
            line = clientFile.readline()
            
            if line == "":
                break
            
            if line == "\n":
                continue
            
            #this is a comment line, it does not represent content
            if line[0] == ';':
                continue
            
            name = line[:-1]
            
            clientList.append(name)
        
        return clientList
    
    def chooseClients(self):
        clientList = self.__getClients()
        random.shuffle(clientList)
        
        clientRepo = ClientRepo()
        for i in range(self.count):
            clientRepo.increaseID()
            clientRepo + Client(clientRepo.ID, clientList[i])
            
        return clientRepo

    
class MovieListGenerator(object):
    def __init__(self):
        self.count = MOVIE_COUNT
        
    def __getMovies(self):
        '''
        Creates a movieList with the data from MOVIE_FILE
        @param:
            - None
        @return:
             - movieList = list of tuples (title, description, genre)
        '''
        movieList = []
        
        filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), MOVIE_FILE)
        movieFile = open(filePath, "r")
    
        while True:
            line = movieFile.readline()
            
            if line == "":
                break
            
            if line == "\n":
                continue
            
            #this is a comment line, it does not represent content
            if line[0] == ';':
                continue
            
            title = line[:-1]
            genre = movieFile.readline()[:-1]
            description = movieFile.readline()[:-1]
            
            movieList.append((title, description, genre))
        
        return movieList
    
    def chooseMovies(self):
        '''
        Randomly selects 10 movies from a movieList
        @param:
            - None
        @return:
            - movieList = object of type MovieRepo
        '''
        movieList = self.__getMovies()
        random.shuffle(movieList)
        
        movieRepo = MovieRepo()
        for i in range(self.count):
            movieRepo.increaseID()
            movieRepo + Movie(movieRepo.ID, movieList[i][0], movieList[i][1], movieList[i][2])
            
        return movieRepo

''''x = ClientListGenerator().chooseClients()
if "John" in x.clientList'''



