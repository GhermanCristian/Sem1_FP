import unittest
from gameEngine import GameEngine
from customExceptions import EmptyError
from constants import COMPUTER_SYMBOL, OCCUPIED_SYMBOL

class TestMove(unittest.TestCase):
    def testPlayerMove(self):
        gameEngine = GameEngine(1,7,7)
        table = gameEngine.getTable()
        
        result = gameEngine.playerMove(1, 1)
        self.assertRaises(EmptyError, gameEngine.playerMove, 0, 0)
        self.assertRaises(EmptyError, gameEngine.playerMove, 0, 1)
        self.assertRaises(EmptyError, gameEngine.playerMove, 0, 2)
        self.assertRaises(EmptyError, gameEngine.playerMove, 2, 0)
        self.assertRaises(EmptyError, gameEngine.playerMove, 1, 1)
        
        self.assertEqual(table.emptyCells, 40)
        self.assertIsNone(result)
        
    def testComputerMove(self):
        gameEngine = GameEngine(1,7,7)
        table = gameEngine.getTable()
        
        result = gameEngine.computerMove()
        self.assertIsNone(result)
        temp = table.emptyCells
        self.assertLess(temp, 49)
        self.assertGreaterEqual(temp, 40)
        
        result = gameEngine.computerMove()
        self.assertIsNone(result)
        self.assertLess(table.emptyCells, temp)
        self.assertGreaterEqual(table.emptyCells, temp - 9)
        
    def testMoveToWin1(self):
        """
        the state of the board before the computer move
        _|_|_
        _|_|_
        _|_|_
        """
        gameEngine = GameEngine(1,3,3)
        table = gameEngine.getTable()

        result = gameEngine.computerMove()
        self.assertEqual(result, COMPUTER_SYMBOL)
        self.assertTrue(table.isFull())
        self.assertEqual(table.emptyCells, 0)
        self.assertEqual(table.getValue(1, 1), COMPUTER_SYMBOL)
        
    def testMoveToWin2(self):
        """
        x|_|_
        _|_|_
        _|_|_
        """
        gameEngine = GameEngine(1,3,3)
        table = gameEngine.getTable()

        table.setValue(0, 0, OCCUPIED_SYMBOL)
        result = gameEngine.computerMove()
        self.assertEqual(result, COMPUTER_SYMBOL)
        self.assertTrue(table.isFull())
        self.assertEqual(table.emptyCells, 0)
        self.assertEqual(table.getValue(1, 1), COMPUTER_SYMBOL)
        
    def testMoveToWin3(self):
        """
        x|x|x
        x|x|_
        x|_|_
        """
        gameEngine = GameEngine(1,3,3)
        table = gameEngine.getTable()

        gameEngine.playerMove(0, 0)
        table.setValue(2, 0, OCCUPIED_SYMBOL)
        table.setValue(0, 2, OCCUPIED_SYMBOL)
        result = gameEngine.computerMove()
        self.assertEqual(result, COMPUTER_SYMBOL)
        self.assertTrue(table.isFull())
        self.assertEqual(table.emptyCells, 0)
        self.assertEqual(table.getValue(2, 2), COMPUTER_SYMBOL)
        
    def testMoveToWin4(self):
        """
        the state of the board before the computer move - in this case, the computer cannot move to win
        _|_|_
        _|x|_
        _|_|_
        """
        gameEngine = GameEngine(1,3,3)
        table = gameEngine.getTable()

        table.setValue(1, 1, OCCUPIED_SYMBOL)
        result = gameEngine.computerMove()
        self.assertIsNone(result)
        self.assertFalse(table.isFull())
        self.assertLessEqual(table.emptyCells, 5)

    def testMoveToWin5(self):
        """
        x|x|x
        x|x|_
        _|_|_
        """
        gameEngine = GameEngine(1,3,3)
        table = gameEngine.getTable()

        gameEngine.playerMove(0, 0)
        table.setValue(0, 2, OCCUPIED_SYMBOL)
        result = gameEngine.computerMove()
        self.assertEqual(result, COMPUTER_SYMBOL)
        self.assertTrue(table.isFull())
        self.assertEqual(table.emptyCells, 0)
        self.assertEqual(table.getValue(2, 1), COMPUTER_SYMBOL)


