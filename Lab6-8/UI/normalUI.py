'''
    The normal, menu-based UI
'''

from constants import MENU_TEXT
from transition import Transition
from customException import EmptyError
from repository import Repository

class UI(object):
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
    def __printData(self, entity, code):
        '''
        Prints a list of objects to the console
        @param:
            - objList = either string, repository or list
        @return:
            - None
        '''        
        if len(entity) == 0:
            print ("Entity is empty")
        
        #string 
        if code == 1:
            print (entity)
            
        #repository
        elif code == 2:
            print (entity)
        
        #mostActive list      
        elif code == 3:
            for i in entity:
                print ("Days rented: " + str(i.daysRented)+ "\n" + str(i))
        
        #lateRentals list
        elif code == 4:
            for i in entity:
                print ("Days past the due date: " + str(i.daysLate()) + "\n" + str(i))
        
        #normal list - search
        elif code == 5:
            for i in entity:
                print (str(i))
                
    def start(self):
        print (MENU_TEXT)
        trans = Transition()
        
        while True:
            userInput = input("Please insert the commandID and the argument list: \n").strip()
            
            if userInput == "0":
                print ("Program has ended")
                return
            
            try:
                if len(userInput) == 0:
                    raise EmptyError("No input")
                userInput = userInput.split()
            except Exception as exc:
                print (str(exc))
                continue
            
            result = trans.call(userInput[0], userInput[1:])
            
            if result == None:
                continue
            else:
                if isinstance(result, str):
                    self.__printData(result, 1)
                elif isinstance(result, Repository):
                    self.__printData(result, 2)
                elif isinstance(result, list):
                    if userInput[0] == "10" or userInput[0] == "11":
                        self.__printData(result, 5)
                    elif userInput[0] == "12":
                        self.__printData(result, 3)
                    elif userInput[0] == "13":
                        self.__printData(result, 4)
            


        