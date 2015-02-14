import random
import base
import kb

class ModeratorFactory(object):
    def __init__(self, choosers):
        self.choosers = choosers
    def __call__(self, possiblefunctions):
        return Moderator(self.choosers,possiblefunctions)

class Moderator(base.BaseRnd):
    def __init__(self, choosers, possiblefunctions,KB=None):
        super(Moderator,self).__init__(possiblefunctions,KB or kb.KB())
        self.choosers = [x(possiblefunctions,self.KB) for x in choosers]
        self.notes = kb.KB()
        self.notes.memory = {}
    def __getgrades__(self, *args, **kwargs):
        grades = [(x,x.__getgrades__(*args, **kwargs)) for x in self.choosers]
        bestperformance = max([self.notes.memory.get(x[0],0) for x in grades])
        bestchooser = random.choice([x for x in grades if self.notes.memory.get(x[0],0) == bestperformance])
        self.lastchooser = bestchooser[0]
        return bestchooser[1]
    def __aftercall__(self,choice,args,kwargs,result):
        old = getattr(self.notes.values,'result',None)
        self.notes.vars.f = choice.func_name
        self.notes.vars.result = result
        self.notes.vars.args = args
        if self.KB.getbest(old,result) != old:
            self.notes.memory[self.lastchooser] = self.notes.memory.get(self.lastchooser,0)+1
        else:
            self.notes.memory[self.lastchooser] = self.notes.memory.get(self.lastchooser,0)-1
        for x in self.choosers:
            x.__aftercall__(choice,args,kwargs,result)
