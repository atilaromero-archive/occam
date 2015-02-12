import types
import random
import functools
import itertools

class Base:
    def __init__(self, possiblefunctions, KB=None):
        """Creates a callable instance that can behave as one of 
        many possible functions. 

        possiblefunctions: function or list of functions.
        KB: anything that __getgrades__ and __choose__ functions undestand or need.
        
        This Base class simply makes a random choice, but subclasses 
        may do better. Hopefully.
        
        After creation, more functions may be added with:
        myinstance.possiblefunctions.append(newfunc)

        Example:
        c will behave like one of these 3 functions.
        >>> c = Base([complex,float,str])

        Call c, like a function
        >>> x = c(1)

        The result, x, is one of (1+0j), 1.0 ,'1'
        >>> x in [(1+0j), 1.0 ,'1']
        True
        """
        self.possiblefunctions = ensurelist(possiblefunctions)
        self.KB = KB
    def __call__(self,*args,**kwargs):
        choice = self.__choose__(*args,**kwargs)
        result = choice(*args,**kwargs)
        self.__aftercall__(choice,args,kwargs,result)
        return result
    def __choose__(self,*args,**kwargs):
        """Will choose only one of the options"""
        grades = self.__getgrades__(*args,**kwargs)
        bestgrade = max([g for f,g in grades])
        assert bestgrade <= 1  # to avoid cheaters
        assert bestgrade >= -1 
        bests = [f for f,g in grades if g == bestgrade]
        return random.choice(bests)
    def __getgrades__(self,*args,**kwargs):
        """Return a list of (function, grade) tuples, 
        where grade is a number in the [-1 , 1] interval."""
        # for this humble base class, all functions deserves a maximun 1.
        return zip(self.possiblefunctions,itertools.repeat(1))
    def __aftercall__(self,choice,args,kwargs,result):
        pass

def ensurelist(possiblefunctions): 
    if callable(possiblefunctions):
        return [possiblefunctions]
    else:
        return list(possiblefunctions) #It can be a set, so let's call list() 
