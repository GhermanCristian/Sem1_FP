import unittest
from gameEngine import GameEngine
from constants import PLAYER_SYMBOL, OCCUPIED_SYMBOL, EMPTY_SYMBOL

class TestTable(unittest.TestCase):
    def testEmptyCells(self):
        gameEngine = GameEngine(1,7,7)
        table = gameEngine.getTable()
        
        self.assertEqual(table.emptyCells, 49)
        gameEngine.playerMove(1, 1)
        self.assertEqual(table.emptyCells, 40)
        gameEngine.playerMove(4, 4)
        self.assertEqual(table.emptyCells, 31)
        gameEngine.playerMove(1, 4)
        self.assertEqual(table.emptyCells, 22)
        gameEngine.playerMove(4, 1)
        self.assertEqual(table.emptyCells, 13)
        gameEngine.playerMove(6, 0)
        self.assertEqual(table.emptyCells, 11)
        gameEngine.playerMove(0, 6)
        self.assertEqual(table.emptyCells, 9)
        gameEngine.playerMove(6, 3)
        self.assertEqual(table.emptyCells, 6)
        gameEngine.playerMove(3, 6)
        self.assertEqual(table.emptyCells, 3)
        gameEngine.computerMove()
        self.assertEqual(table.emptyCells, 0)
        self.assertTrue(table.isFull())
    
    def testTableSize(self):
        gameEngine = GameEngine(1,7,8)
        table = gameEngine.getTable()
        
        self.assertEqual(table.height, 8)
        self.assertEqual(table.width, 7)
        self.assertEqual(table.emptyCells, table.height * table.width)
        self.assertFalse(table.isFull())
        
    def testGetValue(self):
        gameEngine = GameEngine(1,7,8)
        table = gameEngine.getTable()
        
        self.assertEqual(table.getValue(1, 1), EMPTY_SYMBOL)
        
        gameEngine.playerMove(1, 1)
        self.assertEqual(table.getValue(1, 1), PLAYER_SYMBOL)
        self.assertEqual(table.getValue(0, 0), OCCUPIED_SYMBOL)
        self.assertEqual(table.getValue(0, 1), OCCUPIED_SYMBOL)
        self.assertEqual(table.getValue(0, 2), OCCUPIED_SYMBOL)
        self.assertEqual(table.getValue(1, 0), OCCUPIED_SYMBOL)
        self.assertEqual(table.getValue(1, 2), OCCUPIED_SYMBOL)
        self.assertEqual(table.getValue(2, 0), OCCUPIED_SYMBOL)
        self.assertEqual(table.getValue(2, 1), OCCUPIED_SYMBOL)
        self.assertEqual(table.getValue(2, 2), OCCUPIED_SYMBOL)

        self.assertEqual(table.getValue(3,3), EMPTY_SYMBOL)

    def testGetFirstEmpty(self):
        gameEngine = GameEngine(1,7,7)
        table = gameEngine.getTable()
        
        self.assertEqual(table.getFirstEmpty(), (0, 0))
        gameEngine.playerMove(1, 1)
        self.assertEqual(table.getFirstEmpty(), (0, 3))
        gameEngine.playerMove(1, 4)
        self.assertEqual(table.getFirstEmpty(), (0, 6))
        gameEngine.playerMove(1, 6)
        self.assertEqual(table.getFirstEmpty(), (3, 0))
        gameEngine.playerMove(4, 1)
        self.assertEqual(table.getFirstEmpty(), (3, 3))
        gameEngine.playerMove(4, 4)
        self.assertEqual(table.getFirstEmpty(), (3, 6))
        gameEngine.playerMove(4, 6)
        self.assertEqual(table.getFirstEmpty(), (6, 0))
        gameEngine.playerMove(6, 1)
        self.assertEqual(table.getFirstEmpty(), (6, 3))
        gameEngine.playerMove(6, 4)
        self.assertEqual(table.getFirstEmpty(), (6, 6))
        gameEngine.computerMove()
        self.assertTrue(table.isFull())
    
    def testGetAllEmpty(self):
        gameEngine = GameEngine(1,7,7)
        table = gameEngine.getTable()
        
        posList = table.getAllEmpty()
        self.assertEqual(len(posList), 49)
        self.assertEqual(len(posList), table.emptyCells)
        
        gameEngine.playerMove(3, 3)
        posList = table.getAllEmpty()
        self.assertEqual(len(posList), 40)
        
        self.assertEqual(posList[0], (0, 0))
        self.assertEqual(posList[1], (0, 1))
        self.assertEqual(posList[2], (0, 2))
        self.assertEqual(posList[3], (0, 3))
        self.assertEqual(posList[4], (0, 4))
        
        self.assertEqual(posList[35], (6, 2))
        self.assertEqual(posList[36], (6, 3))
        self.assertEqual(posList[37], (6, 4))
        self.assertEqual(posList[38], (6, 5))
        self.assertEqual(posList[39], (6, 6))
        


