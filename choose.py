import random

def rnd(l):
    return random.choice(l)

def choosechoose(options):
    """
    To choose the choosing function
    apply the first choosing funcion on 
    all of them. Please, just make sure 
    the first one isn't too biased.
    """
    return staticmethod(options[0](options))

class Choose:
    choosingoptions = []
    def __init__(self,*options):
        self.options=options
    def __call__(self,*args):
        return Choose.choose(self.options)(*args)
    @staticmethod
    def addChooseFunction(f):
        Choose.choosingoptions.append(f)
        Choose.choose = choosechoose(Choose.choosingoptions)
Choose.addChooseFunction(rnd)
