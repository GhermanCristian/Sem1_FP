from customException import EmptyError

class Repository(object):
    '''
    Fields:
        Public:
            - objList
        Private:
            - __ID
            - __ignoreFlag
    Methods:
        Public:
            - increaseID
            - setIgnoreFlag
        Private:
            - __init__
            - __findByID
            - __add__
            - __delitem__
            - __setitem__
            - __len__
            - __getitem__
            - __contains__
            - __repr__
    Properties:
        - ID
    Setters:
        - None
    '''
    def __init__(self):
        self.objList = []
        self.__ID = 0
        self.__ignoreFlag = False
        
    def __findByID(self, ID):
        '''
        Determines the index in objList of the object with this ID
        @param:
            - ID = integer, or object of type Movie, Client, Rental, if the ignoreFlag is True
        @return:
            - index = integer, or object of type Movie, Client, Rental, if the ignoreFlag is True
        @raise:
            - EmptyError, if the ID is not in the list (and ignoreFlag is False)
        '''
        if self.__ignoreFlag == True:
            return ID
        
        for idx in range(len(self.objList)):
            if self.objList[idx].ID == ID:
                return idx   
        raise EmptyError("No entity with this ID exists")
        
    #+ operator
    def __add__(self, obj):
        self.objList.append(obj)
    
    #del obj[idx]
    def __delitem__(self, ID):
        idx = self.__findByID(ID)
        self.objList.pop(idx)
    
    #obj[idx] = value - I use it as an update
    def __setitem__(self, ID, newObj):
        idx = self.__findByID(ID)
        self.objList.pop(idx)
        self.objList.insert(idx, newObj)
    
    #len(obj) = nr of elements
    def __len__(self):
        return len(self.objList)
    
    #obj[idx]
    def __getitem__(self, ID):
        idx = self.__findByID(ID)
        return self.objList[idx]
    
    #'in' operator - checks if the object is in the list, doesn't work in for loops
    def __contains__(self, obj):
        return obj in self.objList
    
    #used when printing the object
    def __repr__(self):
        toPrint = ""
        for i in self.objList:
            toPrint += str(i) + "\n"
        return toPrint
    
    def increaseID(self):
        self.__ID += 1
    
    #the ignoreFlag is set to True 
    def setIgnoreFlag(self, val):
        self.__ignoreFlag = val
        
    def reset(self):
        self.objList.clear()
        self.__ID = 0
        self.__ignoreFlag = False    
        
    @property
    def ID(self):
        return self.__ID
