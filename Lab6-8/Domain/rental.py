from datetime import datetime

class Rental(object):
    def __init__(self, rentID, clientID, movieID, rentDate, dueDate, returnDate):
        self.__ID = rentID
        self.__clientID = clientID
        self.__movieID = movieID
        self.__rentDate = rentDate
        self.__dueDate = dueDate
        self.__returnDate = returnDate      #useless

    def __str__(self):
        return ("ClientID = " + str(self.__clientID) + " movieID = " + str(self.__movieID) + " from " + str(self.__rentDate) + " to " + str(self.__dueDate) + "\n")
    
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, newValue):
        self.__ID = newValue

    @property
    def clientID(self):
        return self.__clientID
    
    @clientID.setter
    def clientID(self, newValue):
        self.clientID = newValue
        
    @property
    def movieID(self):
        return self.__movieID
    
    @movieID.setter
    def movieID(self, newValue):
        self.movieID = newValue

    @property
    def rentDate(self):
        return self.__rentDate
    
    @rentDate.setter
    def rentDate(self, rentDate):
        self.__rentDate = rentDate

    @property
    def dueDate(self):
        return self.__dueDate
    
    @dueDate.setter
    def dueDate(self, dueDate):
        self.__dueDate = dueDate
        
    def daysLate(self):
        return (datetime.today() - self.__dueDate).days


    
