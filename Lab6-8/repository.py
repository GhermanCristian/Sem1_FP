from customException import EmptyError

class Repository(object):
    def __init__(self):
        self.objList = []
        self.__ID = 0
        self.__ignoreFlag = False
        
    def __findByID(self, ID):
        '''
        Determines the index in objList of the object with this ID
        '''
        if self.__ignoreFlag == True:
            return ID
        
        for i in range(len(self.objList)):
            if self.objList[i].ID == ID:
                return i    
        raise EmptyError("No entity with this ID exists")
        
    "+ operator"
    def __add__(self, obj):
        self.objList.append(obj)
    
    "del obj[idx]"
    def __delitem__(self, ID):
        idx = self.__findByID(ID)
        self.objList.pop(idx)
    
    "obj[idx] = value - I use it as an update"
    def __setitem__(self, ID, newObj):
        idx = self.__findByID(ID)
        self.objList.pop(idx)
        self.objList.insert(idx, newObj)
        
    def __len__(self):
        return len(self.objList)
    
    "obj[idx]"
    def __getitem__(self, ID):
        idx = self.__findByID(ID)
        return self.objList[idx]
    
    "in operator - checks if the object is in the list, doesn't work in for loops"
    def __contains__(self, obj):
        return obj in self.objList
    
    def __repr__(self):
        toPrint = ""
        for i in self.objList:
            toPrint += str(i)
        return toPrint
    
    def increaseID(self):
        self.__ID += 1
        
    def setIgnoreFlag(self, val):
        self.__ignoreFlag = val
        
    '''
    def __iter__(self):
        pass
    '''
        
    @property
    def ID(self):
        return self.__ID