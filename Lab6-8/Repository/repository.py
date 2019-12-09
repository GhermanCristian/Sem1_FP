from Controller.customException import EmptyError

class Repository(object):
    '''
    Class for the repository type (can contain Clients / Movies / Rentals)
    Fields:
        Public:
            - objList
        Private:
            - _ID
            - __ignoreFlag
    Methods:
        Public:
            - increaseID
            - decreaseID
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
            - __iter__
    Properties:
        - ID
    Setters:
        - None
    '''
    def __init__(self, filePath):
        # ID = key; obj = value
        self._objList = {}
        self._ID = 0
        
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
        if isinstance(ID, int) and ID not in self._objList.keys():
            raise EmptyError("No entity with this ID exists")
        
        return True
    
    # depending on which sub class calls this function, this will either write to a file or to pickle
    # (or, if we're working directly with memory, nothing)
    def _save(self):
        pass
    
    #+ operator
    def __add__(self, obj):
        self._objList[obj.ID] = obj
        self._save()
    
    #del obj[idx]
    def __delitem__(self, ID):
        if self.__checkID(ID):
            del self._objList[ID]
        self._save()
    
    #obj[idx] = value - I use it as an update
    def __setitem__(self, ID, newObj):
        if self.__checkID(ID):
            self._objList[ID] = newObj
        self._save()

    #len(obj) = nr of elements
    def __len__(self):
        return len(self._objList)
    
    #obj[idx]
    def __getitem__(self, ID):
        if self.__checkID(ID):
            return self._objList[ID]
    
    #'in' operator - checks if the object is in the list, doesn't work in for loops
    def __contains__(self, obj):
        return obj in self._objList.values()
    
    #used when printing the object
    def __repr__(self):
        toPrint = ""
        for i in self._objList.values():
            toPrint += str(i) + "\n"
        return toPrint
    
    def __iter__(self):
        for i in self._objList.keys():
            yield self._objList[i]
    
    def increaseID(self):
        self._ID += 1
        
    def decreaseID(self):
        self._ID -= 1
        
    def reset(self):
        self._objList.clear()
        self._ID = 0
        
    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self, newID):
        self._ID = newID



