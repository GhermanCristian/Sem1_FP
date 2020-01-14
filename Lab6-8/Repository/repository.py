from Domain.myDict import MyDict

class Repository(MyDict):
    '''
    Class for the repository type (can contain Clients / Movies / Rentals)
    Fields:
        Public:
            - objList
        Private:
            - _ID
            - _crt
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
    def __init__(self):
        MyDict.__init__(self)

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



