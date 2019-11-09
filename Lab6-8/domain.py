'''
    Contains the Movie, Client, Rental types
'''

class Movie(object):
    def __init__(self, ID, title, description, genre):
        self.__daysRented = 0
        self.__ID = ID
        self.__title = title
        self.__description = description
        self.__genre = genre
        
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

class Client(object):
    def __init__(self, ID, name):
        self.__daysRented = 0
        self.__ID = ID
        self.__name = name
        
    def __str__(self):
        return str(self.__ID) + ". " + str(self.__name)
    
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, newID):
        self.__ID = newID 
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name = newName


class Rental(object):
    pass




