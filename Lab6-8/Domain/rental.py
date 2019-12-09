from datetime import date

class Rental(object):
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
    def __init__(self, rentID, clientID, movieID, rentDate, dueDate, returnDate):
        self.__ID = rentID
        self.__clientID = clientID
        self.__movieID = movieID
        self.__rentDate = rentDate
        self.__dueDate = dueDate
        self.__returnDate = returnDate

    def __str__(self):
        return ("ClientID = " + str(self.__clientID) + "; movieID = " + str(self.__movieID) + "; from " + str(self.__rentDate) + " to " + str(self.__dueDate) + "\nReturned - " + str(self.__returnDate) + "\n")
    
    def toText(self):
        return (str(self.__ID) + "\n" + str(self.__clientID) + "\n" + str(self.__movieID) + "\n" + str(self.__rentDate) + "\n" + str(self.__dueDate) + "\n" + str(self.__returnDate) + "\n")

    def __eq__(self, newRental):
        return self.ID == newRental.ID and self.clientID == newRental.clientID and self.movieID == newRental.movieID and self.rentDate == newRental.rentDate and self.dueDate == newRental.dueDate
    
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
    
    @property
    def returnDate(self):
        return self.__returnDate
    
    @returnDate.setter
    def returnDate(self, returnDate):
        self.__returnDate = returnDate
        
    def daysLate(self):
        return (date.today() - self.__dueDate).days


    
