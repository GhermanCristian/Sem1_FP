'''
    Tests for the validator methods
'''

import unittest
from validator import Validator
from customException import RangeError, EmptyError, ArgError, MatchError
from datetime import datetime

class TestValidators(unittest.TestCase):
    
    val = Validator([], [], [])
    
    def testValIndex(self):
        result = self.val.validateIndex("5", 1, 7)
        self.assertEqual(result, 5)
        
        self.assertRaises(ValueError, self.val.validateIndex, "5", "a", 7)
        self.assertRaises(RangeError, self.val.validateIndex, "32", 1, 2)
        self.assertRaises(RangeError, self.val.validateIndex, "32", 20, 10)
        
    def testValDate(self):
        result = self.val.validateDate("20-12-2020")
        self.assertEqual(result, datetime(2020, 12, 20))
        
        self.assertRaises(EmptyError, self.val.validateDate, "")
        self.assertRaises(ValueError, self.val.validateDate, "32-12-2020")
        self.assertRaises(ValueError, self.val.validateDate, "29-02-2021")

        result = self.val.validateDate("2-2-2020")
        self.assertEqual(result, datetime(2020, 2, 2))
        
    def testValAddClient(self):
        result = self.val.valAddClient(["John"])
        self.assertEqual(result, ["John"])
        
        self.assertRaises(EmptyError, self.val.valAddClient, ["a"])
        self.assertRaises(ArgError, self.val.valAddClient, [])
        
        result = self.val.valAddClient(["John Cena"])
        self.assertEqual(result, ["John Cena"])
        
    def testValAddMovie(self):
        result = self.val.valAddMovie(["title1", "desc1", "genre1"])
        self.assertEqual(result, ["title1", "desc1", "genre1"])
        
        self.assertRaises(EmptyError, self.val.valAddMovie, ["ti", "desc1", "genre1"])
        self.assertRaises(EmptyError, self.val.valAddMovie, ["title1", "de", "genre1"])
        self.assertRaises(EmptyError, self.val.valAddMovie, ["title1", "desc1", "ge"])
        
        self.assertRaises(ArgError, self.val.valAddMovie, [])

        result = self.val.valAddMovie(["title1 title1", "desc1 desc1", "genre1 genre1"])
        self.assertEqual(result, ["title1 title1", "desc1 desc1", "genre1 genre1"])
        
    def testValSeparator(self):
        result = self.val.valSeparator(["client"])
        self.assertEqual(result, ["client"])
        
        result = self.val.valSeparator(["movie"])
        self.assertEqual(result, ["movie"])
        
        self.assertRaises(MatchError, self.val.valSeparator, ["clients"])
        self.assertRaises(ArgError, self.val.valSeparator, [])
        
    def testValLateRental(self):
        result = self.val.valLateRentals([])
        self.assertEqual(result, [])
        
        self.assertRaises(ArgError, self.val.valLateRentals, [1])


