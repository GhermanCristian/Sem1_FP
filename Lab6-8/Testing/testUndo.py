'''
    Tests for the undo / redo functionalities
'''
import unittest
from Repository.repository import Repository
from Controller.service import Service
from Domain.client import Client
from Domain.movie import Movie
from Controller.customException import UndoError
from datetime import date

class TestUndo(unittest.TestCase):
    clients = Repository()
    movies = Repository()
    rentals = Repository()
    services = Service(clients, movies, rentals)
    
    def __reset(self):
        self.clients.reset()
        self.movies.reset()
        self.rentals.reset()
    
    def testAddClient(self):
        self.__reset()
        
        self.services.addClient(["Maic"])
        self.services.addClient(["Maichi"])
        self.services.addClient(["Maicuta"])
        self.assertEqual(len(self.clients), 3)
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 2)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        
        self.services.redo([])
        self.assertEqual(len(self.clients), 3)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        
        self.assertRaises(UndoError, self.services.redo, [])
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 2)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        
        self.services.addClient(["Maicq"])
        self.assertRaises(UndoError, self.services.redo, [])
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 2)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 1)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 0)
        self.assertRaises(UndoError, self.services.undo, [])
    
    def testRemoveClient(self):
        self.__reset()
        
        self.services.addClient(["Maic"])
        self.services.addClient(["Maichi"])
        self.services.addClient(["Maicuta"])
        self.services.addMovie(["title", "desc", "genre"])
        self.services.rentMovie([2, 1, date(2019, 11, 20),  date(2019, 11, 29)])
        self.services.returnMovie([2, 1, 1])
        
        self.assertEqual(len(self.clients), 3)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 1)
        
        self.services.removeClient([2])
        self.assertEqual(len(self.clients), 2)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 0)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 3)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 1)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        
        self.services.redo([])
        self.assertEqual(len(self.clients), 2)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 0)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        
        self.assertRaises(UndoError, self.services.redo, [])
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 3)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 1)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        
        self.services.removeClient([1])
        self.assertEqual(len(self.clients), 2)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 1)
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        self.assertRaises(UndoError, self.services.redo, [])
        
        self.services.undo([])
        self.assertEqual(len(self.clients), 3)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 1)
        self.assertEqual(self.clients[1], Client(1, "Maic"))
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        
        self.services.redo([])
        self.assertEqual(len(self.clients), 2)
        self.assertEqual(len(self.movies), 1)
        self.assertEqual(len(self.rentals), 1)
        self.assertEqual(self.clients[2], Client(2, "Maichi"))
        self.assertEqual(self.clients[3], Client(3, "Maicuta"))
        
    def testUpdateClient(self):
        self.__reset()
        
        self.services.addClient(["John"])
        self.assertEqual(self.clients[1].name, "John")
        
        self.services.updateClient([1, "name", "Vasile"])
        self.assertEqual(self.clients[1].name, "Vasile")
        
        self.services.updateClient([1, "name", "Vasileul"])
        self.assertEqual(self.clients[1].name, "Vasileul")
        
        self.services.undo([])
        self.assertEqual(self.clients[1].name, "Vasile")
        
        self.services.redo([])
        self.assertEqual(self.clients[1].name, "Vasileul")
        
        self.services.undo([])
        self.services.undo([])
        self.assertEqual(self.clients[1].name, "John")
        
        self.services.updateClient([1, "name", "Ion"])
        self.assertEqual(self.clients[1].name, "Ion")
        self.assertRaises(UndoError, self.services.redo, [])
    
    def testAddMovie(self):
        self.__reset()
        self.assertEqual(len([]), 0)
        self.__reset()
        self.assertEqual(len([]), 0)
    
    def testRemoveMovie(self):
        self.__reset()
        self.assertEqual(len([]), 0)
        self.__reset()
        self.assertEqual(len([]), 0)
    
    def testUpdateMovie(self):
        self.__reset()
        self.assertEqual(len([]), 0)
        self.__reset()
        self.assertEqual(len([]), 0)
    
    def testRentMovie(self):
        self.__reset()
        self.assertEqual(len([]), 0)
        self.__reset()
        self.assertEqual(len([]), 0)
    
    def testReturnMovie(self):
        self.__reset()
        self.assertEqual(len([]), 0)
        self.__reset()
        self.assertEqual(len([]), 0)


