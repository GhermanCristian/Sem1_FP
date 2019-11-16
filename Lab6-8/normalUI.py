'''
    The normal, menu-based UI
'''

from constants import MENU_TEXT
from transition import Transition
from customException import EmptyError
from clientRepo import ClientRepo
from movieRepo import MovieRepo

class UI(object):
    def __printList(self, objList):
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
            
            '''
            'result' can be a:
                - string, if it's an error message
                - list, if we deal with a command which requires printing
                - None, otherwise (command which doesn't require printing)
            '''
            result = trans.call(userInput[0], userInput[1:])
            
            if result == None:
                continue
            elif isinstance(result, str):
                print (result)
            elif isinstance(result, ClientRepo) or isinstance(result, MovieRepo):
                self.__printList(result)
            


        