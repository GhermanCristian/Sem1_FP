'''
    Contains the Transition type (methods which make the transition from UI to Service)
    Will be used by both the normalUI and the GUI
'''

from validator import Validator
from service import Service
from constants import COMMAND_COUNT
from repository import Repository
from generateList import ClientListGenerator, MovieListGenerator

class Transition(object):
    def __init__(self):
        #This starts the program with procedurally generated lists
        self.clientList = ClientListGenerator().chooseClients()
        self.movieList = MovieListGenerator().chooseMovies()
        self.rentalList = Repository()
        
        self.function = Service(self.clientList, self.movieList, self.rentalList)
        self.functionList = [
            self.function.addClient,
            self.function.removeClient,
            self.function.updateClient,
            self.function.addMovie,
            self.function.removeMovie,
            self.function.updateMovie,
            self.function.getList,
            self.function.rentMovie,
            self.function.returnMovie,
            self.function.searchClients,
            self.function.searchMovies,
            self.function.mostActive,
            self.function.lateRentals,
            self.function.undo,
            self.function.redo
        ]
        
        self.validate = Validator(self.clientList, self.movieList, self.rentalList)
        self.validatorList = [
            self.validate.valAddClient,
            self.validate.valRemClient,
            self.validate.valUpdateClient,
            self.validate.valAddMovie,
            self.validate.valRemMovie,
            self.validate.valUpdateMovie,
            self.validate.valPrintList,
            self.validate.valRentMovie,
            self.validate.valReturnMovie,
            self.validate.valSearch,
            self.validate.valSearch,
            self.validate.valMostActive,
            self.validate.valLateRentals,
            self.validate.valUndo,
            self.validate.valRedo
        ]
    
    def call(self, commandID, argList):
        '''
        Calls the given function, with argList as arguments
        @param:
            - commandID = the ID of the function that has to be called, string
            - argList = list of arguments for that function
        @return:
            - an error message (as a string), if the input is invalid
            - None, if the command doesn't require any printing
            - list to be printed, otherwise
        '''
        
        try:
            commandID = self.validate.validateIndex(commandID, 1, COMMAND_COUNT)
        except Exception as exc:
            return str(exc)
        
        #lists are indexed from 0, but commands are indexed from 1
        commandID -= 1
        
        #parse/ validate the argList
        try:
            argList = self.validatorList[commandID](argList)
        except Exception as exc:
            return str(exc)
        
        try:
            result = self.functionList[commandID](argList)
        except Exception as exc:
            return str(exc)
        
        return result


