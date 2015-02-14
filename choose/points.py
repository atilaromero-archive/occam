import random
import base
import kb

class Points(base.BaseRnd):
    def __init__(self, possiblefunctions,KB=None):
        super(Points,self).__init__(possiblefunctions,KB or kb.KB())
        self.notes = kb.KB()
        self.notes.memory = {}
    def __getgrades__(self, *args, **kwargs):
        bestperformance = max([self.notes.memory.get(x,0) for x in self.possiblefunctions])
        best = random.choice([x for x in self.possiblefunctions if self.notes.memory.get(x,0) == bestperformance])
        return best
    def __aftercall__(self,choice,args,kwargs,result):
        old = getattr(self.notes.values,'result',None)
        self.notes.vars.f = choice.func_name
        self.notes.vars.result = result
        self.notes.vars.args = args
        if self.KB.getbest(old,result) != old:
            self.notes.memory[choice] = self.notes.memory.get(choice,0)+1
        else:
            self.notes.memory[choice] = self.notes.memory.get(choice,0)-1
