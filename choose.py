import random
import functools

def _choosechoose(options):
    """
    To choose the choosing function for the fist time,
    apply the first choosing funcion on all of them.
    Please, just make sure the first one isn't too biased.
    """
    if hasattr(Choose,'choose'):
        choose = Choose.choose
    else:
        choose = options[0]
    return staticmethod(choose(options))

class Choose:
    _choosingoptions = []
    def __init__(self,*options):
        self.options=list(options)
    def __call__(self,*args):
        return Choose._choose(self.options)(*args)
    @staticmethod
    def _addChooseFunction(f):
        Choose._choosingoptions.append(f)
        Choose._choose = _choosechoose(Choose._choosingoptions)

Choose._addChooseFunction(random.choice)

def choose(func):
    return functools.wraps(func)(Choose(func))
