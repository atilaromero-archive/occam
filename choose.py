def _choosechoose(functions):
    """
    To choose the choosing function for the fist time,
    apply the first choosing funcion on all of them.
    Please, just make sure the first one isn't too biased.
    """
    if hasattr(Choose,'choose'):
        choose = Choose.choose
    else:
        choose = functions[0]
    return staticmethod(choose(functions,KB=None))

class Choose:
    _choosingpossiblefunctions = []
    def __init__(self,possiblefunctions,KB=None):
        if callable(possiblefunctions):
            self.possiblefunctions = [possiblefunctions]
        else:
            self.possiblefunctions = list(possiblefunctions)
        self.KB = KB
    def __call__(self,*args,**kwargs):
        choice = Choose._choose(self.possiblefunctions,self.KB)
        return choice(*args,**kwargs)
    def addFunction(self,f):
        self.possiblefunctions.append(f)
        return f
    def withKB(self,KB):
        return Choose(self.possiblefunctions,KB)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
    @staticmethod
    def _chooseFunction(f):
        Choose._choosingpossiblefunctions.append(f)
        Choose._choose = _choosechoose(Choose._choosingpossiblefunctions)
        return f

def withKB(KB):
    def f(func):
        func.KB = KB
        return func
    return f
