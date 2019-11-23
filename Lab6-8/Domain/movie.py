
class Movie(object):
    def __init__(self, ID, title, description, genre):
        self.__daysRented = 0
        self.__ID = ID
        self.__title = title
        self.__description = description
        self.__genre = genre
        self.__isRented = False
        
    def __str__(self):
        return (("ID: %d\nTitle: %s\nGenre: %s\nDescription: %s\n") % (self.ID, self.title, self.genre, self.description))
    
    def __eq__(self, newMovie):
        return self.ID == newMovie.ID and self.title == newMovie.title and self.description == newMovie.description and self.genre == newMovie.genre
        
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
        
    @property
    def daysRented(self):
        return self.__daysRented
    
    @daysRented.setter
    def daysRented(self, newValue):
        self.__daysRented = newValue




