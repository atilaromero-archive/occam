import choose
import functools
import random

def filtercandidates(functions,KB=None):
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
        choose.Choose.memory[move] = (KB.getbest(old,new) != old)
        return new
    return f

choose.Choose.memory = {}
@choose.Choose._chooseFunction
def choosegoodbad(functions,KB=None):
    candidates = filtercandidates(functions,KB=KB)
    goods = [x for x in choose.Choose.memory.keys() if x in candidates and choose.Choose.memory[x]]
    if len(goods)>0:
        move = random.choice(goods)
    else:
        move = random.choice(functions)
    print move
    if len(filtercandidates([_recordmove],KB=KB))>0:
        move = _recordmove(move,KB)
    return move
