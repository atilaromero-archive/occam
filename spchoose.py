import sympy
import choose
import KB

class SPChoose(choose.Choose):
    def __init__(self,functions):
        self.possiblefunctions = choose.ensurelist(functions)
        self.KB = KB.KB()
        self.KB.memory = {}
    def _choose(self,*args,**kwargs):
        #checks if f is memory and have performed well
        goods = [f for f in self.possiblefunctions if self.KB.memory.get(f,False) == True]
        if len(goods)>0:
            move = random.choice(goods)
        else:
            move = random.choice(self.possiblefunctions)
        print move
        move = _recordmove(move,self.KB)
        return move

def _recordmove(move,KB):
    @functools.wraps(move)
    def f(*args,**kwargs):
        old = KB.getstate()
        move(*args,**kwargs)
        new = KB.getstate()
        KB.memory[move] = (KB.getbest(old,new) != old)
        return new
    return f
