import sympy
import random
import functools
import choose
import KB

class SPChoose(choose.Choose):
    def __init__(self,functions):
        self.possiblefunctions = choose.ensurelist(functions)
        self.KB = KB.KB()
        self.KB.memory = {}
    def _choose(self,*args,**kwargs):
        #checks if f is in memory and have performed well
        goods = [f for f in self.possiblefunctions if self.KB.memory.get(f,False) == True]
        if len(goods)>0:
            choice = random.choice(goods)
        else:
            choice = random.choice(self.possiblefunctions)
        return choice
    def __aftercall__(self,choice,args,kwargs,result):
        self.KB.vars.f = choice.func_name
        old = getattr(self.KB.values,'result',None)
        self.KB.vars.result = result
        self.KB.vars.args = args
        self.KB.memory[choice] = (self.KB.getbest(old,result) != old)
