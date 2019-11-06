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
        return str(self.ID) + ". " + str(self.Title) + " - " + str(self.Genre) + "\n" + str(self.Description) 
        
    @property
    def ID(self):
        return self.__ID    
        
    @property
    def Title(self):
        return self.__title
    
    @property
    def Description(self):
        return self.__description
    
    @property
    def Genre(self):
        return self.__genre    
        
    def updateMovie(self, title, description, genre):
        '''
        Updates all fields of a movie
        !! it's too similiar to a __init__
        @param:
            - title = new movie title
            - description = new movie description
            - genre = new movie genre
        @return:
            - None
        '''
        self.__title = title
        self.__description = description
        self.__genre = genre

class Client(object):
    def __init__(self, ID, name):
        self.__daysRented = 0
        self.__ID = ID
        self.__name = name
        
    def __str__(self):
        return str(self.ID) + ". " + str(self.Name)
    
    @property
    def ID(self):
        return self.__ID
    
    @property
    def Name(self):
        return self.__name
    
    def updateClient(self, name):
        '''
        '''
        self.__name = name


class Rental(object):
    pass

x = Movie(1, "aaa", "bbb", "ccc")
print (x)
x.update(x.Title, "new desc", x.Genre)
print (x)
y = Client(1, "john")
print (y)



