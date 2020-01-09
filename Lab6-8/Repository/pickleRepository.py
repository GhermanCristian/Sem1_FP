import pickle
from Repository.repository import *

class PickleRepository(Repository):
    def __init__(self, filePath):
        Repository.__init__(self)
        self.__filePath = filePath
        self.__loadPickle()
        
    #reads from binary file
    def __loadPickle(self):
        try:
            file = open(self.__filePath, "rb")
            self._objList = pickle.load(file)
            
            for ID in self._objList:
                if ID > self._ID:
                    self._ID = ID
            
            file.close()
        
        except EOFError:
            self._objList = {}
        
    #writes to binary file
    def _save(self):
        file = open(self.__filePath, "wb")
        pickle.dump(self._objList, file)
        file.close()


