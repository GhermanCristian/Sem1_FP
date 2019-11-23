import unittest
from generateList import MovieListGenerator
from Domain.movie import Movie

class TestMovie(unittest.TestCase):
    
    def testAdd(self):
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.movieID = self.movieRepo.ID
        self.movieRepo.setIgnoreFlag(True)
        
        self.movieRepo.increaseID()
        self.movieRepo + Movie(self.movieRepo.ID, "Title1", "Desc1", "Genre1")
        self.movieRepo.increaseID()
        self.movieRepo + Movie(self.movieRepo.ID, "Title2", "Desc2", "Genre2")
        self.movieRepo.increaseID()
        self.movieRepo + Movie(self.movieRepo.ID, "Title3", "Desc3", "Genre3")
        self.movieRepo.increaseID()
        self.movieRepo + Movie(self.movieRepo.ID, "Title4", "Desc4", "Genre4")
        self.movieRepo.increaseID()
        self.movieRepo + Movie(self.movieRepo.ID, "Title5", "Desc5", "Genre5")
        
        self.assertEqual(len(self.movieRepo), self.movieID + 5)
        self.assertEqual(self.movieRepo.ID, self.movieID + 5)
        
        self.assertEqual(self.movieRepo[self.movieID], Movie(self.movieID + 1, "Title1", "Desc1", "Genre1"))
        self.assertEqual(self.movieRepo[self.movieID + 1], Movie(self.movieID + 2, "Title2", "Desc2", "Genre2"))
        self.assertEqual(self.movieRepo[self.movieID + 2], Movie(self.movieID + 3, "Title3", "Desc3", "Genre3"))
        self.assertEqual(self.movieRepo[self.movieID + 3], Movie(self.movieID + 4, "Title4", "Desc4", "Genre4"))
        self.assertEqual(self.movieRepo[self.movieID + 4], Movie(self.movieID + 5, "Title5", "Desc5", "Genre5"))
    
    def testRemove(self):
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.movieCount = self.movieRepo.ID
        self.movieRepo.setIgnoreFlag(True)
        
        del self.movieRepo[0]
        del self.movieRepo[0]
        del self.movieRepo[0]
        
        self.assertEqual(len(self.movieRepo), self.movieCount - 3)
        self.assertEqual(self.movieRepo[0].ID, 4)
        self.assertEqual(self.movieRepo[1].ID, 5)
        self.assertEqual(self.movieRepo[2].ID, 6)
        
        del self.movieRepo[0]
        del self.movieRepo[0]
        del self.movieRepo[0]
        
        self.assertEqual(len(self.movieRepo), self.movieCount - 6)
        self.assertEqual(self.movieRepo[0].ID, 7)
        self.assertEqual(self.movieRepo[1].ID, 8)
        self.assertEqual(self.movieRepo[2].ID, 9)
    
    def testUpdate(self):
        self.movieRepo = MovieListGenerator().chooseMovies()
        self.movieID = self.movieRepo.ID
        self.movieRepo.setIgnoreFlag(True)
        
        self.movieRepo.increaseID()
        self.movieRepo[0] = Movie(self.movieRepo.ID, "Title1", "Desc1", "Genre1")
        self.movieRepo.increaseID()
        self.movieRepo[1] = Movie(self.movieRepo.ID, "Title2", "Desc2", "Genre2")
        self.movieRepo.increaseID()
        self.movieRepo[2] = Movie(self.movieRepo.ID, "Title3", "Desc3", "Genre3")
        self.movieRepo.increaseID()
        self.movieRepo[3] = Movie(self.movieRepo.ID, "Title4", "Desc4", "Genre4")
        self.movieRepo.increaseID()
        self.movieRepo[4] = Movie(self.movieRepo.ID, "Title5", "Desc5", "Genre5")
        
        self.assertEqual(len(self.movieRepo), self.movieID)
        self.assertEqual(self.movieRepo.ID, self.movieID + 5)

        self.assertEqual(self.movieRepo[0], Movie(self.movieID + 1, "Title1", "Desc1", "Genre1"))
        self.assertEqual(self.movieRepo[1], Movie(self.movieID + 2, "Title2", "Desc2", "Genre2"))
        self.assertEqual(self.movieRepo[2], Movie(self.movieID + 3, "Title3", "Desc3", "Genre3"))
        self.assertEqual(self.movieRepo[3], Movie(self.movieID + 4, "Title4", "Desc4", "Genre4"))
        self.assertEqual(self.movieRepo[4], Movie(self.movieID + 5, "Title5", "Desc5", "Genre5"))






