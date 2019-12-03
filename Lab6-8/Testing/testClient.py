import unittest
from Generators.generateClients import ClientListGenerator
from Domain.client import Client
from service import Service

class TestClient(unittest.TestCase):

    def testAdd(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.service = Service(self.clientRepo, [], [])
        self.lastID = self.clientRepo.ID
        
        self.service.addClient(["Hamilton"])
        self.service.addClient(["Bottas"])
        self.service.addClient(["Verstappen"])
        self.service.addClient(["Leclerc"])
        self.service.addClient(["Vettel"])
        
        self.assertEqual(self.clientRepo.ID, self.lastID + 5)
        self.assertEqual(len(self.clientRepo), self.lastID + 5)
        
        self.assertEqual(self.clientRepo[self.lastID + 1], Client(self.lastID + 1, "Hamilton"))
        self.assertEqual(self.clientRepo[self.lastID + 2], Client(self.lastID + 2, "Bottas"))
        self.assertEqual(self.clientRepo[self.lastID + 3], Client(self.lastID + 3, "Verstappen"))
        self.assertEqual(self.clientRepo[self.lastID + 4], Client(self.lastID + 4, "Leclerc"))
        self.assertEqual(self.clientRepo[self.lastID + 5], Client(self.lastID + 5, "Vettel"))
        
    def testRemove(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.lastID = self.clientRepo.ID       #initially the nr of clients = ID of the last client = .ID
        
        del self.clientRepo[1]
        del self.clientRepo[2]
        del self.clientRepo[3]
        
        self.assertEqual(len(self.clientRepo), self.lastID - 3)
        self.assertEqual(self.clientRepo[4].ID, 4)
        self.assertEqual(self.clientRepo[5].ID, 5)
        self.assertEqual(self.clientRepo[6].ID, 6)
        
        del self.clientRepo[4]
        del self.clientRepo[5]
        del self.clientRepo[6]
        
        self.assertEqual(len(self.clientRepo), self.lastID - 6)
        self.assertEqual(self.clientRepo[7].ID, 7)
        self.assertEqual(self.clientRepo[8].ID, 8)
        self.assertEqual(self.clientRepo[9].ID, 9)
        
    def testUpdate(self):
        self.clientRepo = ClientListGenerator().chooseClients()
        self.lastID = self.clientRepo.ID       #initially the nr of clients = ID of the last client = .ID
        self.service = Service(self.clientRepo, [], [])
                
        self.service.updateClient([1, "name", "Albon"])
        self.service.updateClient([2, "name", "Gasly"])
        self.service.updateClient([3, "name", "Kimi"])
        self.service.updateClient([4, "name", "Ricciardo"])
        self.service.updateClient([5, "name", "Sainz"])
        
        self.assertEqual(len(self.clientRepo), self.lastID)
        self.assertEqual(self.clientRepo.ID, self.lastID)
        
        self.assertEqual(self.clientRepo[1], Client(1, "Albon"))
        self.assertEqual(self.clientRepo[2], Client(2, "Gasly"))
        self.assertEqual(self.clientRepo[3], Client(3, "Kimi"))
        self.assertEqual(self.clientRepo[4], Client(4, "Ricciardo"))
        self.assertEqual(self.clientRepo[5], Client(5, "Sainz"))




