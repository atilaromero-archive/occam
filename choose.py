import random

def choosechoose(options):
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
    choosingoptions = []
    def __init__(self,*options):
        self.options=list(options)
    def __call__(self,*args):
        return Choose.choose(self.options)(*args)
    @staticmethod
    def addChooseFunction(f):
        Choose.choosingoptions.append(f)
        Choose.choose = choosechoose(Choose.choosingoptions)

Choose.addChooseFunction(random.choice)
