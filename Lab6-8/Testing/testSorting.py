'''
    Tests for the sorting functionalities (most active clients, most rented movies, late rentals)
'''

import unittest
from repository import Repository
from Domain.client import Client
from Domain.movie import Movie
from Domain.rental import Rental
from service import Service
from datetime import datetime

class TestSorting(unittest.TestCase):
    
    clients = Repository()
    movies = Repository()
    rentals = Repository()
    service = Service(clients, movies, rentals)
    
    service.addClient(["John"])
    service.addClient(["Mike"])
    service.addClient(["Nike"])
    
    Client1 = Client(1, "John")
    Client2 = Client(2, "Mike")
    Client3 = Client(3, "Nike")
    
    service.addMovie(["Title1", "Desc1", "Genre1"])
    service.addMovie(["Title2", "Desc2", "Genre2"])
    service.addMovie(["Title3", "Desc3", "Genre3"])
    
    Movie1 = Movie(1, "Title1", "Desc1", "Genre1")
    Movie2 = Movie(2, "Title2", "Desc2", "Genre2")
    Movie3 = Movie(3, "Title3", "Desc3", "Genre3")
    
    def testActiveClients(self):
        self.service.rentMovie([1, 1, datetime(2019, 10, 20), datetime(2019, 10, 29)])
        self.service.rentMovie([2, 2, datetime(2019, 11, 20), datetime(2019, 11, 30)])
        
        self.service.returnMovie([1, 1, 0])
        self.service.rentMovie([3, 1, datetime(2019, 10, 30), datetime(2019, 11, 12)])
        
        self.service.returnMovie([3, 1, 1])
        self.service.returnMovie([2, 2, 0])
        
        result = self.service.mostActive(["client"])
        self.assertEqual(result, [self.Client1, self.Client3, self.Client2])
        self.assertEqual(len(self.rentals), 0)
        
        self.rentals.reset()
    
    def testRentedMovies(self):
        self.service.rentMovie([1, 1, datetime(2019, 10, 20), datetime(2019, 10, 29)])
        self.service.rentMovie([2, 2, datetime(2019, 11, 20), datetime(2019, 11, 30)])
        
        self.service.returnMovie([1, 1, 0])
        self.service.rentMovie([3, 1, datetime(2019, 10, 30), datetime(2019, 11, 12)])
        
        self.service.returnMovie([3, 1, 1])
        self.service.returnMovie([2, 2, 0])
        
        result = self.service.mostActive(["movie"])
        self.assertEqual(result, [self.Movie1, self.Movie2, self.Movie3])
        self.assertEqual(len(self.rentals), 0)
        
        self.rentals.reset()
    
    def testLateRentals(self):
        self.service.rentMovie([1, 1, datetime(2019, 10, 20), datetime(2019, 10, 29)])
        self.service.rentMovie([2, 2, datetime(2019, 11, 20), datetime(2019, 11, 24)])
        self.service.rentMovie([3, 3, datetime(2018, 10, 20), datetime(2018, 10, 29)])
        
        Rental1 = Rental(1, 1, 1, datetime(2019, 10, 20), datetime(2019, 10, 29), None)
        Rental2 = Rental(2, 2, 2, datetime(2019, 11, 20), datetime(2019, 11, 24), None)
        Rental3 = Rental(3, 3, 3, datetime(2018, 10, 20), datetime(2018, 10, 29), None)
        
        result = self.service.lateRentals([])
        
        self.assertEqual(result, [Rental3, Rental1, Rental2])
        
        self.service.returnMovie([3, 3, 2])
        self.service.returnMovie([2, 2, 1])
        self.service.returnMovie([1, 1, 0])
        
        self.assertEqual(len(self.rentals), 0)
        self.rentals.reset()



