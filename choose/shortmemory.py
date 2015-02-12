import sympy
import random
import functools
import base
import KB

class ShortMemory(base.Base):
    def __init__(self,functions):
        self.possiblefunctions = base.ensurelist(functions)
        self.KB = KB.KB()
        self.KB.memory = {}
    def __getgrades__(self,*args,**kwargs):
        grades = []
        for f in self.possiblefunctions:
            registry = self.KB.memory.get(f,0)
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
        self.KB.vars.f = choice.func_name
        old = getattr(self.KB.values,'result',None)
        self.KB.vars.result = result
        self.KB.vars.args = args
        self.KB.memory[choice] = (self.KB.getbest(old,result) != old)
