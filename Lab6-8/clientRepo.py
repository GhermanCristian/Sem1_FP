'''
'''

class ClientRepo(object):
    def __init__(self):
        self.clientList = []
        self.clientID = 0
        
    "+ operator"
    def __add__(self, client):
        self.clientList.append(client)
    
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
        
    @property
    def ID(self):
        return self.clientID
        