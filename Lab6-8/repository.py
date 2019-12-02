from customException import EmptyError

class Repository(object):
    '''
    Class for the repository type (can contain Clients / Movies / Rentals)
    Fields:
        Public:
            - objList
        Private:
            - __ID
            - __ignoreFlag
    Methods:
        Public:
            - increaseID
            - decreaseID
            - setIgnoreFlag
            - reset
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
        # ID = key; obj = value
        self.__objList = {}
        self.__ID = 0
        self.__ignoreFlag = False
        
    def __checkID(self, ID):
        '''
        Determines the index in objList of the object with this ID
        @param:
            - ID = integer, or object of type Movie, Client, Rental, if the ignoreFlag is True
        @return:
            - index = integer, or object of type Movie, Client, Rental, if the ignoreFlag is True
        @raise:
            - EmptyError, if the ID is not in the list (and ignoreFlag is False)
        '''     
        if isinstance(ID, int) and ID not in self.__objList.keys():
            raise EmptyError("No entity with this ID exists")
        
        return True
    
    #+ operator
    def __add__(self, obj):
        self.__objList[obj.ID] = obj
    
    #del obj[idx]
    def __delitem__(self, ID):
        if self.__checkID(ID):
            del self.__objList[ID]
    
    #obj[idx] = value - I use it as an update
    def __setitem__(self, ID, newObj):
        if self.__checkID(ID):
            self.__objList[ID] = newObj
    
    #len(obj) = nr of elements
    def __len__(self):
        return len(self.__objList)
    
    #obj[idx]
    def __getitem__(self, ID):
        if self.__checkID(ID):
            return self.__objList[ID]
    
    #'in' operator - checks if the object is in the list, doesn't work in for loops
    def __contains__(self, obj):
        return obj in self.__objList.values()
    
    #used when printing the object
    def __repr__(self):
        toPrint = ""
        for i in self.__objList.values():
            toPrint += str(i) + "\n"
        return toPrint
    
    def __iter__(self):
        for i in self.__objList.keys():
            yield self.__objList[i]
    
    def increaseID(self):
        self.__ID += 1
        
    def decreaseID(self):
        self.__ID -= 1
    
    def setIgnoreFlag(self, val):
        self.__ignoreFlag = val
        
    def reset(self):
        self.__objList.clear()
        self.__ID = 0
        self.__ignoreFlag = False
        
    @property
    def ID(self):
        return self.__ID



