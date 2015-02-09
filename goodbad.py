import choose
import functools
import random

class GoodBad(choose.Choose):
    def __init__(self,functions,KB=None):
        self.possiblefunctions = choose.ensurelist(functions)
        self.KB = KB
        if self.KB is None:
            self.KB = type('KB', (), {})() #creates an instance of a empty class
        if not hasattr(KB,'memory'):
            KB.memory = {}
    def _choose(self):
        candidates = filtercandidates(self.possiblefunctions,self.KB)
        goods = [x for x in candidates if self.KB.memory.get(x,False) == True]
        if len(goods)>0:
            move = random.choice(goods)
        else:
            move = random.choice(self.possiblefunctions)
            print move
        if len(filtercandidates([_recordmove],self.KB))>0:
            move = _recordmove(move,self.KB)
        return move

def filtercandidates(functions,KB):
    candidates = []
    for c in functions:
        if hasattr(c,'need'):
            if all([x in dir(KB) for x in c.need]):
                candidates.append(c)
        else:
            candidates.append(c)
    return candidates

def need(lst):
    def f(func):
        func.need = lst
        return func
    return f

@need(['getstate','getbest'])
def _recordmove(move,KB):
    @functools.wraps(move)
    def f(*args,**kwargs):
        old = KB.getstate()
        move(*args,**kwargs)
        new = KB.getstate()
        KB.memory[move] = (KB.getbest(old,new) != old)
        return new
    return f

