from constants import MOVIE_COUNT, MOVIE_FILE
import random
from Domain.movie import Movie
from Repository.repository import Repository

class MovieListGenerator(object):
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
        movieFile = open(MOVIE_FILE, "r")
    
        while True:
            line = movieFile.readline()
            
            #end of file
            if line == "":
                break
            
            #empty line
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
        Randomly selects MOVIE_COUNT movies from a movieList
        @param:
            - None
        @return:
            - movieList = object of type MovieRepo
        '''
        movieList = self.__getMovies()
        random.shuffle(movieList)
        
        movieRepo = Repository("")
        for i in range(self.count):
            movieRepo.increaseID()
            movieRepo + Movie(movieRepo.ID, movieList[i][0], movieList[i][1], movieList[i][2])
            
        return movieRepo
