'''
'''

class MovieRepo(object):
    def __init__(self):
        self.movieList = []
        self.movieID = 0
        
    "+ operator"
    def __add__(self, movie):
        self.movieList.append(movie)
    
    "del obj[idx]"
    def __delitem__(self, idx):
        self.movieList.pop(idx)
    
    "obj[idx] = value"    
    def __setitem__(self, idx, newMovie):
        self.movieList.pop(idx)
        self.movieList.insert(idx, newMovie)
        
    def __len__(self):
        return len(self.movieList)
    
    "obj[idx]"
    def __getitem__(self, idx):
        return self.movieList[idx]
    
    def increaseID(self):
        self.movieID += 1
        
    @property
    def ID(self):
        return self.movieID