import types
import random
import functools

class Choose:
    def __init__(self, choosefunction, possiblefunctions, KB=None):
        """Creates a callable instance that can behave as one of 
        many possible functions. 
        possiblefunctions: function or list of functions
        choosefunction: will choose which one, probably using KB(Knowledge Base)
        KB: anything that choosefunction undestands or needs
        
        After creation, more functions may be added with:
        myinstance.possiblefunctions.append(newfunc)

        Example:
        c will behave like one of these 3 functions.
        We didn't use KB in _choose, so it's None.
        >>> c = Choose(rnd,[complex,float,str],None)

        Call c, like a function
        >>> x = c(1)

        The result, x, is one of (1+0j), 1.0 ,'1'
        >>> x in [(1+0j), 1.0 ,'1']
        True
        """
        self.possiblefunctions = ensurelist(possiblefunctions)
        self.KB = KB
        self._choose = types.MethodType(choosefunction,self)
    def __call__(self,*args,**kwargs):
        choice = self._choose(*args,**kwargs)
        result = choice(*args,**kwargs)
        self.__aftercall__(choice,args,kwargs,result)
        return result
    def __aftercall__(self,choice,args,kwargs,result):
        pass
    def withKB(self,KB):       #with requirement
        "with myinstance.withKB(newKB) as newinstance:"
        return self.__class__(self.possiblefunctions,KB,self.choosefunction)
    def __enter__(self):       #with requirement
        return self
    def __exit__(self, *args): #with requirement
        pass

def ensurelist(possiblefunctions): 
    if callable(possiblefunctions):
        return [possiblefunctions]
    else:
        return list(possiblefunctions) #It can be a set, so let's call list() 
   
def rnd(self,*args,**kwargs): 
    return random.choice(self.possiblefunctions)
