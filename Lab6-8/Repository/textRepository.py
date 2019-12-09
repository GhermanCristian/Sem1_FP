from Repository.repository import *
from Domain.client import Client
from Domain.movie import Movie
from Domain.rental import Rental
from datetime import date

class TextRepository(Repository):
    def __init__(self, filePath):
        Repository.__init__(self, filePath)
        
        if "client" in filePath:
            self.__entityType = "client"
        elif "movie" in filePath:
            self.__entityType = "movie"
        elif "rental" in filePath:
            self.__entityType = "rental"
            
        #this will store the comments in each file (lines starting with ';') so that they don't get overwritten
        self.__auxText = ""
        self.__filePath = filePath
        self.__loadFile()
        
    def __loadFile(self):
        file = open(self.__filePath, "r")
        
        while True:
            line = file.readline()
            
            #end of file
            if line == "":
                break
            
            #empty line
            if line == "\n":
                continue
            
            #this is a comment line, it does not represent content
            if line[0] == ';':
                self.__auxText += line
                continue
            
            ID = int(line[:-1])
            
            if self.__entityType == "client":
                name = file.readline()[:-1]
                self._objList[ID] = Client(ID, name)
            
            elif self.__entityType == "movie":
                title = file.readline()[:-1]
                genre = file.readline()[:-1]
                description = file.readline()[:-1]
                self._objList[ID] = Movie(ID, title, genre, description)
            
            elif self.__entityType == "rental":
                clientID = int(file.readline()[:-1])
                movieID = int(file.readline()[:-1])
                
                rentDate = file.readline()[:-1]
                rentDate = date.fromisoformat(rentDate)
                
                dueDate = file.readline()[:-1]
                dueDate = date.fromisoformat(dueDate)
                
                returnDate = file.readline()
                
                if "None" in returnDate:
                    returnDate = None
                else:
                    try:
                        returnDate = date.fromisoformat(returnDate)
                    except:
                        returnDate = date.fromisoformat(returnDate[:-1])
    
                self._objList[ID] = Rental(ID, clientID, movieID, rentDate, dueDate, returnDate)

            if self.ID < ID:
                self.ID = ID
        
        file.close()
        
    def _save(self):
        file = open(self.__filePath, "w")
        
        file.write(self.__auxText)
        file.write("\n")
        
        IDList = []
        for entity in self._objList:
            IDList.append(entity)
        IDList.sort()
        
        for ID in IDList:
            file.write(self._objList[ID].toText() + "\n")
            
        file.close()    
    
    
    
    
    