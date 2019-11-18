import unittest
from generateList import ClientListGenerator
from domain import Client

class TestClient(unittest.TestCase):

    def testAdd(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.clientID = self.clientRepo.ID
        
        self.clientRepo.increaseID()
        self.clientRepo + Client(self.clientRepo.ID, "Hamilton")
        self.clientRepo.increaseID()
        self.clientRepo + Client(self.clientRepo.ID, "Bottas")
        self.clientRepo.increaseID()
        self.clientRepo + Client(self.clientRepo.ID, "Verstappen")
        self.clientRepo.increaseID()
        self.clientRepo + Client(self.clientRepo.ID, "Leclerc")
        self.clientRepo.increaseID()
        self.clientRepo + Client(self.clientRepo.ID, "Vettel")
        
        self.assertEqual(self.clientRepo.ID, self.clientID + 5)
        self.assertEqual(len(self.clientRepo), self.clientID + 5)
        
        self.assertEqual(self.clientRepo[self.clientID], Client(self.clientID + 1, "Hamilton"))
        self.assertEqual(self.clientRepo[self.clientID + 1], Client(self.clientID + 2, "Bottas"))
        self.assertEqual(self.clientRepo[self.clientID + 2], Client(self.clientID + 3, "Verstappen"))
        self.assertEqual(self.clientRepo[self.clientID + 3], Client(self.clientID + 4, "Leclerc"))
        self.assertEqual(self.clientRepo[self.clientID + 4], Client(self.clientID + 5, "Vettel"))
        
    def testRemove(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.clientCount = self.clientRepo.ID       #initially the nr of clients = ID of the last client = .ID
        
        del self.clientRepo[0]
        del self.clientRepo[0]
        del self.clientRepo[0]
        
        self.assertEqual(len(self.clientRepo), self.clientCount - 3)
        self.assertEqual(self.clientRepo[0].ID, 4)
        self.assertEqual(self.clientRepo[1].ID, 5)
        self.assertEqual(self.clientRepo[2].ID, 6)
        
        del self.clientRepo[0]
        del self.clientRepo[0]
        del self.clientRepo[0]
        
        self.assertEqual(len(self.clientRepo), self.clientCount - 6)
        self.assertEqual(self.clientRepo[0].ID, 7)
        self.assertEqual(self.clientRepo[1].ID, 8)
        self.assertEqual(self.clientRepo[2].ID, 9)
        
    def testUpdate(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.clientID = self.clientRepo.ID       #initially the nr of clients = ID of the last client = .ID
        
        self.clientRepo.increaseID()
        self.clientRepo[0] = Client(self.clientRepo.ID, "Albon")
        self.clientRepo.increaseID()
        self.clientRepo[1] = Client(self.clientRepo.ID, "Gasly")
        self.clientRepo.increaseID()
        self.clientRepo[2] = Client(self.clientRepo.ID, "Kimi")
        self.clientRepo.increaseID()
        self.clientRepo[3] = Client(self.clientRepo.ID, "Ricciardo")
        self.clientRepo.increaseID()
        self.clientRepo[4] = Client(self.clientRepo.ID, "Sainz")
        
        self.assertEqual(len(self.clientRepo), self.clientID)
        self.assertEqual(self.clientRepo.ID, self.clientID + 5)
        
        self.assertEqual(self.clientRepo[0], Client(self.clientID + 1, "Albon"))
        self.assertEqual(self.clientRepo[1], Client(self.clientID + 2, "Gasly"))
        self.assertEqual(self.clientRepo[2], Client(self.clientID + 3, "Kimi"))
        self.assertEqual(self.clientRepo[3], Client(self.clientID + 4, "Ricciardo"))
        self.assertEqual(self.clientRepo[4], Client(self.clientID + 5, "Sainz"))




