import random
import functools
import inspect
import types
import decorator

###
#  Auxiliary functions
###

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
    return staticmethod(choose(options,intel=None))

def mayberemoveintelfromkwargs(func,kwargs):
    if type(func) == types.InstanceType:
        argspect = inspect.getargspec(func.__call__)
    else:
        argspect = inspect.getargspec(func)
    if 'intel' in argspect.args or argspect.keywords != None:
        return kwargs
    else:
        kwargs2 = dict(kwargs)
        del kwargs2['intel']
        return kwargs2

def need(lst):
    def f(func):
        func.need = lst
        return func
    return f

def filtercandidates(options,intel=None):
    candidates = []
    for c in options:
        if hasattr(c,'need'):
            if all([x in dir(intel) for x in c.need]):
                candidates.append(c)
        else:
            candidates.append(c)
    return candidates

class Intel:
    def __repr__(self):
        return str([x for x in dir(self) if not x.startswith('_')])
###
#  End of auxiliary functions
###

class Choose:
    _choosingoptions = []
    def __init__(self,*options):
        self.options=list(options)
    def __call__(self,*args,**kwargs):
        intel = None
        if 'intel' in kwargs.keys():
            intel = kwargs['intel']
        choice = Choose._choose(self.options,intel=intel)
        kwargs2 = mayberemoveintelfromkwargs(choice,kwargs)
        return choice(*args,**kwargs2)
    @staticmethod
    def _chooseFunction(f):
        Choose._choosingoptions.append(f)
        Choose._choose = _choosechoose(Choose._choosingoptions)
        return f
    def addOption(self,f):
        self.options.append(f)
        return f

Choose.memory = {}

@Choose._chooseFunction
def choosegoodbad(options,intel=None):
    candidates = filtercandidates(options,intel=intel)
    goods = [x for x in Choose.memory.keys() if x in candidates and Choose.memory[x]]
    if len(goods)>0:
        move = random.choice(goods)
    else:
        move = random.choice(options)
    print move
    @need(['getstate','getbest'])
    @functools.wraps(move)
    def _recordmove(*args,**kwargs):
        old = intel.getstate()
        kwargs2 = mayberemoveintelfromkwargs(move,kwargs)
        move(*args,**kwargs2)
        new = intel.getstate()
        Choose.memory[move] = (intel.getbest(old,new) != old)
        return new
    results = filtercandidates([_recordmove],intel=intel)
    if len(results) == 0:
        results.append(move)
    return random.choice(results)

