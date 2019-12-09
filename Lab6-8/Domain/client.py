class Client(object):
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
    def __init__(self, ID, name):
        self.__daysRented = 0
        self.__ID = ID
        self.__name = name
        
    def __str__(self):
        return ("ID: %d\nName: %s\n") % (self.ID, self.name)
    
    def __eq__(self, newClient):
        return self.ID == newClient.ID and self.name == newClient.name
    
    def toText(self):
        return ("%d\n%s\n") % (self.ID, self.name)
    
    @property
    def ID(self):
        return self.__ID
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name = newName
        
    @property
    def daysRented(self):
        return self.__daysRented
    
    @daysRented.setter
    def daysRented(self, newValue):
        self.__daysRented = newValue


