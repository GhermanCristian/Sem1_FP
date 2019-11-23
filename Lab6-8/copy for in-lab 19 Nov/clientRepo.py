'''
'''

class ClientRepo(object):
    def __init__(self):
        self.clientList = []
        self.clientID = 0
        #
        self.countDuplicates = []
        
    "+ operator"
    def __add__(self, client):
        self.clientList.append(client)
        #
        self.countDuplicates.append(0)
    
    "del obj[idx]"
    def __delitem__(self, idx):
        self.clientList.pop(idx)
    
    "obj[idx] = value"    
    def __setitem__(self, idx, newClient):
        self.clientList.pop(idx)
        self.clientList.insert(idx, newClient)
        
    def __len__(self):
        return len(self.clientList)
    
    "obj[idx]"
    def __getitem__(self, idx):
        return self.clientList[idx]
    
    def increaseID(self):
        self.clientID += 1
        
    def inside(self, nameValue):
        for i in range(len(self.clientList) - 2, 0, -1):
            if nameValue in self.clientList[i].name:
                return i
        return None
        
    @property
    def ID(self):
        return self.clientID

