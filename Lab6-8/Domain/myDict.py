from Controller.customException import EmptyError

class MyDict(object):
    def __init__(self):
        # ID = key; obj = value
        self._objList = {}
        self._ID = 0
        self._crt = 0
        
    def __checkID(self, ID):
        '''
        Determines the index in objList of the object with this ID
        @param:
            - ID = integer, or object of type Movie, Client, Rental
        @return:
            - index = integer, or object of type Movie, Client, Rental, if the ignoreFlag is True
        @raise:
            - EmptyError, if the ID is not in the list (and ignoreFlag is False)
        '''     
        if isinstance(ID, int) and ID not in self._objList.keys():
            raise EmptyError("No entity with this ID exists")
        
        return True
    
    # depending on which sub class calls this function, this will either write to a file or to pickle
    # (or, if we're working directly with memory, nothing)
    def _save(self):
        pass
    
    #+ operator
    def __add__(self, obj):
        self._objList[obj.ID] = obj
        self._save()
    
    #del obj[idx]
    def __delitem__(self, ID):
        if self.__checkID(ID):
            del self._objList[ID]
        self._save()
    
    #obj[idx] = value - I use it as an update
    def __setitem__(self, ID, newObj):
        if self.__checkID(ID):
            self._objList[ID] = newObj
        self._save()

    #len(obj) = nr of elements
    def __len__(self):
        return len(self._objList)
    
    #obj[idx]
    def __getitem__(self, ID):
        if self.__checkID(ID):
            return self._objList[ID]
    
    #'in' operator - checks if the object is in the list, doesn't work in for loops
    def __contains__(self, obj):
        return obj in self._objList.values()
    
    #used when printing the object
    def __repr__(self):
        toPrint = ""
        for i in self._objList.values():
            toPrint += str(i) + "\n"
        return toPrint
   
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._crt > self._ID:
            self._crt = 0
            raise StopIteration
    
        self._crt += 1
        
        while self._crt <= self._ID:
            if self._crt in self._objList.keys():
                return self._objList[self._crt]
            self._crt += 1
            
        self._crt = 0
        raise StopIteration
    
    def filter(self, filterFunction, val, isID):
        auxList = []
        
        for obj in self._objList.values():
            if filterFunction(isID, val, obj) == True:
                auxList.append(obj)
                
        if isID == True and len(auxList) == 0:
            raise EmptyError("No entity with this ID")
        
        return auxList
    
    def __flip(self, auxList, end):
        '''
        Flips the first 'end' elements of a list
        @param:
            - auxList = list
            - end = integer
        @return:
            - the modified list
        @raise:
            - None
        '''
        x = auxList[end::-1]
        x.extend(auxList[end + 1: ])
        return x
    
    def __maxPosition(self, auxList, end, cmp):
        '''
        Determines the position of the maximum element in the [0, end] range ('end' is included)
        *maximum in relation with the cmp function
        @param:
            - auxlist = list
            - end = integer, the right bound of the range in which we search
            - cmp = function which figures out how to sort 2 elements
        @return:
            - maxPos = integer, position of the maximum element
        @raise:
            - None
        '''
        maxVal = auxList[0]
        maxPos = 0
        
        for i in range(1, end + 1):
            if cmp(maxVal, auxList[i]) == True:
                maxVal = auxList[i]
                maxPos = i
        
        return maxPos
    
    def sort(self, cmp):
        '''
        Returns a sorted list of the objects in this data structure
        -> Pancake sort
        @param:
            - cmp = function which figures out how to sort 2 elements
        @return:
            - auxlist = sorted list of the objects in this repository
        '''
        auxList = []
        for i in self._objList.values():
            auxList.append(i)

        #we place each maximum value at the end of the current range, and then we decrease the range (similar to selection sort)
        #'end' is the right bound of this range
        end = len(auxList) - 1
        while end > 0:
            maxPos = self.__maxPosition(auxList, end, cmp)
            #the element is already where it needs to be => we don't need to move it
            if maxPos == end:
                end -= 1
                continue
            
            #to place an element at the end of the range, we first move it to the first position in the list
            #by flipping the range [0, maxPos]; then, to get it to the last position, we flip the entire range
            if maxPos != 0:
                #if it is already on the first position, there's no need to do the first flip
                auxList = self.__flip(auxList, maxPos)
            auxList = self.__flip(auxList, end)
            end -= 1
    
        return auxList
    




