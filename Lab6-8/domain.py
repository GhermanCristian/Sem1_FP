'''
    Contains the Movie, Client, Rental types
'''

from datetime import date

class Movie(object):
    def __init__(self, ID, title, description, genre):
        self.__daysRented = 0
        self.__ID = ID
        self.__title = title
        self.__description = description
        self.__genre = genre
        self.__isRented = False
        #rentMovie will set this to True, returnMovie will set it back to False
        
    def __str__(self):
        return str(self.__ID) + ". " + str(self.__title) + " - " + str(self.__genre) + "\n" + str(self.__description) 
      
    # i should overload this to also work with an additional parameter (same for client)
    # maybe use a default argument = None ? 
        
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, newID):
        self.__ID = newID    
        
    @property
    def title(self):
        return self.__title    
        
    @title.setter
    def title(self, newTitle):
        self.__title = newTitle
        
    @property
    def description(self):
        return self.__description    
        
    @description.setter
    def description(self, newDescription):
        self.__description = newDescription
        
    @property
    def genre(self):
        return self.__genre    
        
    @genre.setter
    def genre(self, newGenre):
        self.__genre = newGenre
        
    @property
    def isRented(self):
        return self.__isRented
    
    @isRented.setter
    def isRented(self, newValue):
        self.__isRented = newValue


class Client(object):
    def __init__(self, ID, name):
        self.__daysRented = 0
        self.__ID = ID
        self.__name = name
        self.__rentals = [] #list of Rental objects
        
    '''
    This function will print the ID of a client, not its place in the current list
    '''
    def __str__(self):
        return str(self.__ID) + ". " + str(self.__name)
    
    @property
    def ID(self):
        return self.__ID
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name = newName
        
    def canRent(self):
        '''
        Checks if the client can rent a movie
        @param:
            - None
        @return:
            - True, if the client can rent movies
            - False, otherwise
        '''
        crtDate = date.today()
        for rental in self.__rentedMovies:
            if rental.dueDate > crtDate:
                return False
            
        return True
    
    def addRental(self, rentalObj):
        '''
        Adds a new movie to the rentedMovies list
        @param:
            - movie, of type Movie
        @return:
            - None
        '''
        self.__rentals.append(rentalObj)
        
    def returnMovie(self, movie):
        '''
        Removes a movie from the rentedMovies list
        @param:
            - movie, of type Movie
        @return:
            - None
        '''
        for i in range(len(self.__rentedMovies)):
            if movie == self.__rentedMovies[i]:
                self.__rentedMovies.pop(i)

class Rental(object):
    '''
        How does the user rent a movie:
        - clientID, movieID and dueDate are provided by the user
        - rentDate is implicit = the current date (due - rent <= 14 days)
        How does the user return a movie:
        - clientID and movieID
    '''
    def __init__(self, rentID, clientID, movieID, rentDate, dueDate, returnDate):
        self.ID = rentID
        self.clientID = clientID
        self.movieID = movieID
        self.rentDate = rentDate
        self.dueDate = dueDate
        self.returnDate = returnDate

    @property
    def dueDate(self):
        return self.__dueDate

