import random
import functools
import inspect

class Intel:
    pass

def _choosechoose(options):
    """
    To choose the choosing function for the fist time,
    apply the first choosing funcion on all of them.
    Please, just make sure the first one isn't too biased.
    """
    print '---> calling _choosechoose'
    if hasattr(Choose,'choose'):
        choose = Choose.choose
    else:
        choose = options[0]
    intel = Intel()
    intel.lowlevelchoosefunction = None
    return staticmethod(choose(options,intel=intel))

class Choose:
    _choosingoptions = []
    def __init__(self,*options):
        self.options=list(options)
    def __call__(self,*args,**kwargs):
        'print calling Choose.__call__'
        intel = None
        if 'intel' in kwargs.keys():
            intel = kwargs['intel']
        choice = Choose._choose(self.options,intel=intel)
        if type(choice) == types.InstanceType:
            argspect = inspect.getargspec(choice.__call__)
        else:
            argspect = inspect.getargspec(choice)
        if 'intel' in argspect.args or argspect.keywords != None:
            return choice(*args,**kwargs)
        else:
            kwargs2 = dict(kwargs)
            del kwargs2['intel']
            return choice(*args,**kwargs2)
        else:
            
    @staticmethod
    def _chooseFunction(f):
        Choose._choosingoptions.append(f)
        Choose._choose = _choosechoose(Choose._choosingoptions)
        return f
    def addOption(self,f):
        self.options.append(f)
        return f

def need(lst):
    def f(func):
        func.need = lst
        return func
    return f

def filtercandidates(intel,options):
    candidates = []
    print 'filtering','intel:',intel,'options:',options
    for c in options:
        if hasattr(c,'need'):
            if all([x for x in c.need if x in dir(intel)]):
                candidates.append(c)
        else:
            candidates.append(c)
    return candidates

@Choose._chooseFunction
@need(['lowlevelchoosefunction'])
def chooseonintel_rnd(intel,options):
    print 'calling chooseonintel_rnd',intel,options
    candidates = filtercandidates(intel,options)
    print 'candidates',candidates
    return random.choice(candidates)

@Choose._chooseFunction
@need(['getstate','getbest'])
def choosegoodbad(intel,options):
    print 'calling choosegoodbad', intel, options
    goods = [x for x in Choose.memory.keys() if x in options and Choose.memory[x]]
    if len(goods)>0:
        move = random.choice(goods)
    else:
        move = random.choice(options)
    @functools.wraps(move)
    def _recordmove(*args,**kwargs):
        old = intel.getstate()
        print move,intel,args
        move(*args,**kwargs)
        new = intel.getstate()
        Choose.memory[move] = (intel.getbest(old,new) != old)
        return new
    return _recordmove
Choose.memory = {}

@Choose
def loop(intel,func):
    print 'calling loop'
    result = intel.getstate()
    print result
    while not intel.goal(result):
        func(intel)
        result = intel.getstate()
        print result
    return result


from equilibrium import A,B,C,D,E,F,piece

intel = Intel()
intel.getstate = piece.getvalue
intel.goal = near_zero
intel.getbest = bestnum
choosemove = Choose(A,B,C,D,E,F)

def test():
    print 'calling teste'
    return choosemove(intel)

def testloop():
    return loop(intel,intel,choosemove)

def near_zero(x):
    return -1 < x and x < 1

def bestnum(x,y):
    if abs(x)<abs(y):
        return x
    else:
        return y

