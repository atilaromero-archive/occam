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
    def __call__(self,*args,**kwargs):
        return self.getChoice()(*args,**kwargs)
    def getChoice(self):
        return Choose._choose(self.options)
    @staticmethod
    def _addChooseFunction(f):
        Choose._choosingoptions.append(f)
        Choose._choose = _choosechoose(Choose._choosingoptions)

#Choose._addChooseFunction(random.choice)

def choosegoodbad(options):
    goods = [x for x in Choose.memory.keys() if x in options and Choose.memory[x]]
    if len(goods)>0:
        return random.choice(goods)
    else:
        return random.choice(options)

Choose.memory = {}

Choose._addChooseFunction(choosegoodbad)

