from constants import CLIENT_COUNT, CLIENT_FILE
import random
from Domain.client import Client
from Repository.repository import Repository

class ClientListGenerator(object):
    '''
    Class for the 
    Fields:
        Public:
            - None
        Private:
            - None
    Methods:
        Public:
            - None
        Private:
            - None
    Properties:
        - None
    Setters:
        - None
    '''
    def __init__(self):
        self.count = CLIENT_COUNT
    
    def __getClients(self):
        '''
        Creates a clientList with the data from CLIENT_FILE
        @param:
            - None
        @return:
             - clientList = list of tuples (title, description, genre)
        '''
        clientList = []
        clientFile = open(CLIENT_FILE, "r")
    
        while True:
            line = clientFile.readline()
            
            #end of file
            if line == "":
                break
            
            #empty line
            if line == "\n":
                continue
            
            #this is a comment line, it does not represent content
            if line[0] == ';':
                continue
            
            name = line[:-1]
            
            clientList.append(name)
        
        return clientList
    
    def chooseClients(self):
        '''
        Randomly selects CLIENT_COUNT clients from a clientList 
        '''
        clientList = self.__getClients()
        random.shuffle(clientList)
        
        clientRepo = Repository()
        for i in range(self.count):
            clientRepo.increaseID()
            clientRepo + Client(clientRepo.ID, clientList[i])
            
        return clientRepo


