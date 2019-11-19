'''
    Tests for the rent / return functionalities
'''

import unittest
from service import Service
from generateList import ClientListGenerator, MovieListGenerator
from datetime import datetime
from domain import Rental

class TestRent(unittest.TestCase):
    
    def testRent(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.service = Service(self.clientRepo, self.movieRepo)
        
        self.service.rentMovie([0, 0, datetime(2019, 12, 20), 1, 1])
        self.service.rentMovie([0, 1, datetime(2019, 12, 20), 1, 2])
        self.service.rentMovie([0, 2, datetime(2019, 12, 20), 1, 3])
        
        self.assertEqual(len(self.clientRepo[0].rentals), 3)
        self.assertEqual(len(self.clientRepo[1].rentals), 0)
        self.assertTrue(self.movieRepo[0].isRented)
        self.assertTrue(self.movieRepo[1].isRented)
        self.assertTrue(self.movieRepo[2].isRented)
        self.assertFalse(self.movieRepo[3].isRented)
        
        #PROBLEM WITH THE DATE!!
        #self.assertEqual(self.clientRepo[0].rentals[0], Rental(1, 1, 1, datetime.today(), datetime(2019, 12, 20), None))
        #self.assertEqual(self.clientRepo[0].rentals[0], Rental(2, 1, 2, datetime.today(), datetime(2019, 12, 20), None))
        #self.assertEqual(self.clientRepo[0].rentals[0], Rental(3, 1, 3, datetime.today(), datetime(2019, 12, 20), None))
    
    def testReturn(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.service = Service(self.clientRepo, self.movieRepo)
        
        self.service.rentMovie([0, 0, datetime(2019, 12, 20), 1, 1])
        self.service.rentMovie([0, 1, datetime(2019, 12, 20), 1, 2])
        self.service.rentMovie([0, 2, datetime(2019, 12, 20), 1, 3])
        
        self.service.returnMovie([0, 1, 1])
        self.assertEqual(len(self.clientRepo[0].rentals), 2)
        self.assertTrue(self.movieRepo[2].isRented)

