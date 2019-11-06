'''
    The normal, menu-based UI
'''

from validator import Validator
from customException import RangeError
from service import Service

class UI(object):
    def __init__(self):
        self.MENU_TEXT = """
            Command list:
            0. Exit
            1. Add new client
                - 
            2. Remove client
                -
            3. Update client
                - 
            4. Add new movie
                - 
            5. Remove movie
                -
            6. Update movie
                -  
            7. List
                - "client"
                - "movie"
            9. Rent a movie
                - 
            10. Return a movie
                - 
            11. *search
            12. *statistics
            . undo / redo
        """
        self.service = Service()
        self.commandList = [
            self.service.addClient, 
            self.service.removeClient,
            self.service.updateClient,
            self.service.addMovie,
            self.service.removeMovie,
            self.service.updateMovie,
            self.service.printAll
        ]
    
    def printAll(self, objList):
        '''
        Prints a list of objects to the console
        @param:
            - objList = list of either movies or clients
        @return:
            - None
        '''
        if len(objList) == 0:
            print ("List is empty")
            
        else:
            for i in objList:
                print (i)
                
    def start(self):
        print (self.MENU_TEXT)
        
        valid = Validator()
        
        while True:
            break
            index = input("Please insert command:\n")
            try:
                index = valid.validateIndex(index, 0, 12)
            except TypeError as err:
                pass
            except RangeError:
                print(RangeError)
            
            if index == 0:
                print ("Program has ended")
                return 
            
            
            
            self.commandList[index](paramList)
            


        