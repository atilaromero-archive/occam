import sympy
import random
import functools
import base
import kb

class ShortMemory(base.BaseRnd):
    def __init__(self,functions,KB=None):
        super(ShortMemory,self).__init__(functions,KB or kb.KB())
        self.notes = kb.KB()
        self.notes.memory = {}
    def __getgrades__(self,*args,**kwargs):
        grades = []
        for f in self.possiblefunctions:
            registry = self.notes.memory.get(f,0)
            if registry == 0: # not in memory
                grades.append(0)
            elif registry == False:
                grades.append(-1)
            elif registry == True:
                grades.append(1)
            else:
                raise ValueError(registry)
        return zip(self.possiblefunctions,grades)
    def __aftercall__(self,choice,args,kwargs,result):
        old = getattr(self.notes.values,'result',None)
        self.notes.vars.f = choice.func_name
        self.notes.vars.result = result
        self.notes.vars.args = args
        self.notes.memory[choice] = (self.KB.getbest(old,result) != old)
