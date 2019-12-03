import unittest
from Generators.generateMovies import MovieListGenerator
from Domain.movie import Movie
from service import Service

class TestMovie(unittest.TestCase):
    
    def testAdd(self):
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.movieID = self.movieRepo.ID
        self.service = Service([], self.movieRepo, [])
        
        self.service.addMovie(["Title1", "Desc1", "Genre1"])
        self.service.addMovie(["Title2", "Desc2", "Genre2"])
        self.service.addMovie(["Title3", "Desc3", "Genre3"])
        self.service.addMovie(["Title4", "Desc4", "Genre4"])
        self.service.addMovie(["Title5", "Desc5", "Genre5"])
        
        self.assertEqual(len(self.movieRepo), self.movieID + 5)
        self.assertEqual(self.movieRepo.ID, self.movieID + 5)
        
        self.assertEqual(self.movieRepo[self.movieID + 1], Movie(self.movieID + 1, "Title1", "Desc1", "Genre1"))
        self.assertEqual(self.movieRepo[self.movieID + 2], Movie(self.movieID + 2, "Title2", "Desc2", "Genre2"))
        self.assertEqual(self.movieRepo[self.movieID + 3], Movie(self.movieID + 3, "Title3", "Desc3", "Genre3"))
        self.assertEqual(self.movieRepo[self.movieID + 4], Movie(self.movieID + 4, "Title4", "Desc4", "Genre4"))
        self.assertEqual(self.movieRepo[self.movieID + 5], Movie(self.movieID + 5, "Title5", "Desc5", "Genre5"))
    
    def testRemove(self):
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.movieCount = self.movieRepo.ID
        
        del self.movieRepo[1]
        del self.movieRepo[2]
        del self.movieRepo[3]
        
        self.assertEqual(len(self.movieRepo), self.movieCount - 3)
        self.assertEqual(self.movieRepo[4].ID, 4)
        self.assertEqual(self.movieRepo[5].ID, 5)
        self.assertEqual(self.movieRepo[6].ID, 6)
        
        del self.movieRepo[4]
        del self.movieRepo[5]
        del self.movieRepo[6]
        
        self.assertEqual(len(self.movieRepo), self.movieCount - 6)
        self.assertEqual(self.movieRepo[7].ID, 7)
        self.assertEqual(self.movieRepo[8].ID, 8)
        self.assertEqual(self.movieRepo[9].ID, 9)
    
    def testUpdate(self):
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.movieID = self.movieRepo.ID
        self.service = Service([], self.movieRepo, [])
        
        self.service.updateMovie([1, "title", "Title1"])
        self.service.updateMovie([2, "title", "Title2"])
        self.service.updateMovie([3, "title", "Title3"])
        self.service.updateMovie([4, "title", "Title4"])
        self.service.updateMovie([5, "title", "Title5"])
        
        self.service.updateMovie([1, "description", "Desc1"])
        self.service.updateMovie([2, "description", "Desc2"])
        self.service.updateMovie([3, "description", "Desc3"])
        self.service.updateMovie([4, "description", "Desc4"])
        self.service.updateMovie([5, "description", "Desc5"])
        
        self.service.updateMovie([1, "genre", "Genre1"])
        self.service.updateMovie([2, "genre", "Genre2"])
        self.service.updateMovie([3, "genre", "Genre3"])
        self.service.updateMovie([4, "genre", "Genre4"])
        self.service.updateMovie([5, "genre", "Genre5"])
        
        self.assertEqual(len(self.movieRepo), self.movieID)
        self.assertEqual(self.movieRepo.ID, self.movieID)

        self.assertEqual(self.movieRepo[1], Movie(1, "Title1", "Desc1", "Genre1"))
        self.assertEqual(self.movieRepo[2], Movie(2, "Title2", "Desc2", "Genre2"))
        self.assertEqual(self.movieRepo[3], Movie(3, "Title3", "Desc3", "Genre3"))
        self.assertEqual(self.movieRepo[4], Movie(4, "Title4", "Desc4", "Genre4"))
        self.assertEqual(self.movieRepo[5], Movie(5, "Title5", "Desc5", "Genre5"))






