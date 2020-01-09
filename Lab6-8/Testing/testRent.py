'''
    Tests for the rent / return functionalities
'''

import unittest
from Controller.service import Service
from Generators.generateClients import ClientListGenerator
from Generators.generateMovies import MovieListGenerator 
from datetime import date
from Repository.repository import Repository

class TestRent(unittest.TestCase):
    clients = ClientListGenerator().chooseClients()
    movies = MovieListGenerator().chooseMovies()
    
    def testRent(self):
        self.rentals = Repository()
        self.service = Service(self.clients, self.movies, self.rentals)
        
        self.service.rentMovie([1, 1, date(2019, 11, 12), date(2019, 11, 15)])
        self.assertTrue(self.movies[1].isRented)
        self.assertEqual(len(self.rentals), 1)
        self.assertEqual(self.rentals[1].rentDate, date(2019, 11, 12))
        self.assertEqual(self.rentals[1].dueDate, date(2019, 11, 15))
        self.assertEqual(self.rentals[1].clientID, 1)
        self.assertEqual(self.rentals[1].movieID, 1)
        
        self.service.rentMovie([2, 2, date(2019, 11, 12), date(2019, 11, 15)])
        self.assertTrue(self.movies[2].isRented)
        self.assertEqual(len(self.rentals), 2)
        self.assertEqual(self.rentals[2].rentDate, date(2019, 11, 12))
        self.assertEqual(self.rentals[2].dueDate, date(2019, 11, 15))
        self.assertEqual(self.rentals[2].clientID, 2)
        self.assertEqual(self.rentals[2].movieID, 2)
    
    def testReturn(self):
        self.rentals = Repository()
        self.service = Service(self.clients, self.movies, self.rentals)
        
        self.service.rentMovie([1, 1, date(2019, 11, 12), date(2019, 11, 15)])
        self.service.rentMovie([2, 2, date(2019, 11, 12), date(2019, 11, 15)])
        self.service.rentMovie([3, 3, date(2019, 11, 12), date(2019, 11, 15)])
        self.service.rentMovie([4, 4, date(2019, 11, 12), date(2019, 11, 15)])
        
        self.service.returnMovie([1, 1, 1])
        self.assertFalse(self.movies[1].isRented)
        self.assertEqual(len(self.rentals), 4)
        self.assertIsNotNone(self.rentals[1].returnDate)
        
        self.service.returnMovie([3, 3, 3])
        self.assertFalse(self.movies[3].isRented)
        self.assertEqual(len(self.rentals), 4)
        self.assertIsNotNone(self.rentals[3].returnDate)
        
        self.assertTrue(self.movies[2].isRented)
        self.assertTrue(self.movies[4].isRented)
