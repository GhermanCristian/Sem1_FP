from customException import UndoError

class UndoController(object):
    '''
    Class for the undo/redo functionalities
    Fields:
        Public:
            - None
        Private:
            - __actionList
            - __idx
    Methods:
        Public:
            - addAction
            - undo
            - redo
        Private:
            - __init__
    Properties:
        - None
    Setters:
        - None
    '''
    def __init__(self):
        #actionList will contain tuples of the form (actionID, revArgList, normArgList)
        self.__actionList = []
        self.__idx = 0
        
    def addAction(self, actionID, revArgList, normArgList):
        self.__idx += 1
        
        #when adding a new action to the list, the "redo" part of the list is deleted
        while len(self.__actionList) >= self.__idx:
            self.__actionList.pop()
        
        #revArgList is the argument list used by the reverse function (when doing undo)
        #normArgList is the argument list used by the normal function (when doing redo)
        #    - basically this will always be the original argList
        self.__actionList.append((actionID, revArgList, normArgList))
        
    def undo(self):
        if self.__idx <= 0:
            raise UndoError("No more undo operations left")
        
        self.__idx -= 1
        return self.__actionList[self.__idx]
    
    def redo(self):
        if self.__idx >= len(self.__actionList):
            raise UndoError("No more redo operations left")
        
        action = self.__actionList[self.__idx]
        self.__idx += 1
        return action

