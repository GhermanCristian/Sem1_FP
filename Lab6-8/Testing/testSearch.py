'''
    Test for the search client / search movie functionalities
'''

import unittest
from Domain.client import Client
from Domain.movie import Movie
from service import Service
from repository import Repository
from customException import EmptyError

class TestSearch(unittest.TestCase):
    def testSearchClient(self):
        self.clients = Repository()
        self.service = Service(self.clients, [], Repository())
        
        self.service.addClient(["John"])
        self.service.addClient(["Mike"])
        self.service.addClient(["zmaili"])
        self.service.addClient(["Johnny"])
        
        result = self.service.searchClients([2, True])
        self.assertEqual(result, [self.clients[2]])
        self.assertEqual(len(self.clients), 4)
        self.assertEqual(self.clients[2], Client(2, "Mike"))
        
        result = self.service.searchClients(["john", False])
        self.assertEqual(result, [self.clients[1], self.clients[4]])
        self.assertEqual(len(self.clients), 4)
        self.assertEqual(self.clients[1], Client(1, "John"))
        self.assertEqual(self.clients[4], Client(4, "Johnny"))
        
        result = self.service.searchClients(["luca", False])
        self.assertEqual(result, [])
        self.assertEqual(len(self.clients), 4)
        
        self.assertRaises(EmptyError, self.service.searchClients, ["john", True])
        
        self.service.removeClient([2])
        self.assertRaises(EmptyError, self.service.searchClients, [2, True])
        
        result = self.service.searchClients([3, True])
        self.assertEqual(result, [self.clients[3]])
        self.assertEqual(len(self.clients), 3)
        self.assertEqual(self.clients[3], Client(3, "zmaili"))
    
    def testSearchMovie(self):
        self.movies = Repository()
        self.service = Service([], self.movies, Repository())

        self.service.addMovie(["title1", "desc1", "genre1"])
        self.service.addMovie(["tiitle2", "deesc2", "geenre2"])
        self.service.addMovie(["title 3", "desc 3", "genre 3"])
        
        result = self.service.searchMovies(["title", False])
        self.assertEqual(result, [self.movies[1], self.movies[3]])
        self.assertEqual(len(self.movies), 3)
        self.assertEqual(self.movies[1], Movie(1, "title1", "desc1", "genre1"))
        self.assertEqual(self.movies[2], Movie(2, "tiitle2", "deesc2", "geenre2"))
        self.assertEqual(self.movies[3], Movie(3, "title 3", "desc 3", "genre 3"))

        result = self.service.searchMovies(["taitle", False])
        self.assertEqual(result, [])
        self.assertEqual(len(self.movies), 3)
        
        self.service.removeMovie([2])
        self.assertRaises(EmptyError, self.service.searchMovies, [2, True])
        
        self.assertRaises(EmptyError, self.service.searchMovies, ["john", True])
        
        result = self.service.searchMovies([3, True])
        self.assertEqual(result, [self.movies[3]])
        self.assertEqual(len(self.movies), 2)
        self.assertEqual(self.movies[1], Movie(1, "title1", "desc1", "genre1"))
        self.assertEqual(self.movies[3], Movie(3, "title 3", "desc 3", "genre 3"))

        result = self.service.searchMovies(["tITlE", False])
        self.assertEqual(result, [self.movies[1], self.movies[3]])
        self.assertEqual(len(self.movies), 2)
        self.assertEqual(self.movies[1], Movie(1, "title1", "desc1", "genre1"))
        self.assertEqual(self.movies[3], Movie(3, "title 3", "desc 3", "genre 3"))
