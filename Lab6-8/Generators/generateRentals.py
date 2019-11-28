import random
from datetime import date, timedelta
from constants import RENTAL_COUNT
from repository import Repository
from validator import Validator
from service import Service

class RentalListGenerator(object):
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
    def __init__(self, clients, movies):
        self.clients = clients
        self.movies = movies
        self.clientCount = len(self.clients)
        self.movieCount = len(self.movies)
        
        self.rentals = Repository()
        self.service = Service(self.clients, self.movies, self.rentals)
        self.val = Validator(self.clients, self.movies, self.rentals)
        
    def __generatePastRental(self, isLate):
        '''
        Generates a Rental that has been done and due in the past, and which is or is not returned
        '''
        #both date1 and date2 need to be 'random' days in the past, date1 < date2
        client = random.randint(1, self.clientCount)
        movie = random.randint(1, self.movieCount)
        nrOfDays = random.randint(1, 500)
        
        date1 = date.today() - timedelta(nrOfDays)
        date2 = date.today() - timedelta(nrOfDays - random.randint(3, 5))
                
        try:
            self.val.canRent(client)
            if self.movies[movie].isRented == True:
                return False
        except:
            return False
        
        self.service.rentMovie([client, movie, date1, date2])
        if not isLate:
            self.service.returnMovie([client, movie, len(self.rentals) - 1])
        
        return True
    
    def __generateCurrentRental(self):
        '''
        Generates a Rental that is currently active, but not late
        '''
        client = random.randint(1, self.clientCount)
        movie = random.randint(1, self.movieCount)
        
        date1 = date.today() - timedelta(random.randint(1, 10))
        date2 = date.today() + timedelta(random.randint(1, 10))
        
        try:
            self.val.canRent(client)
            if self.movies[movie].isRented == True:
                return False
        except:
            return False
        
        self.service.rentMovie([client, movie, date1, date2])
        self.service.returnMovie([client, movie, len(self.rentals) - 1])
        
        return True

    def generateList(self):
        for i in range(RENTAL_COUNT // 2):
            result = False
            while result == False:
                result = self.__generateCurrentRental()
        
        for i in range(RENTAL_COUNT // 2):
            result = False
            while result == False:
                result = self.__generatePastRental(random.randint(0, 1))
                
        return self.rentals

