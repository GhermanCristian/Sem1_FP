import os

class Settings(object):
    def __init__(self):
        self.repoType = ""
        self.clients = ""
        self.movies = ""
        self.rentals = ""
        self.UI = ""
        
        self.__loadData()
        
    def __loadData(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        file = open("settings.properties", "r")
        
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
                continue
            
            auxList = line.split("=")
            auxList[0] = auxList[0].strip()
            auxList[1] = auxList[1].strip()
            
            if auxList[0][0:3] == "rep":
                self.repoType = auxList[1][1:-1]
                
                if self.repoType != "memory":
                    os.chdir(os.path.join(os.getcwd(), "Data"))
            
            elif auxList[0][0] == "c":
                self.clients = auxList[1][1:-1]
                
                if len(self.clients) != 0:
                    self.clients = os.path.join(os.getcwd(), self.clients)
            
            elif auxList[0][0] == "m":
                self.movies = auxList[1][1:-1]
                
                if len(self.movies) != 0:
                    self.movies = os.path.join(os.getcwd(), self.movies)
            
            elif auxList[0][0:3] == "ren":
                self.rentals = auxList[1][1:-1]
                
                if len(self.rentals) != 0:
                    self.rentals = os.path.join(os.getcwd(), self.rentals)
                
            elif auxList[0][0] == "u":
                self.UI = auxList[1][1:-1]
                
        file.close()        


