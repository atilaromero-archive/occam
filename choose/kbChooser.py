import base
import kb

class KBChooser(base.BaseRnd):
    """A generic class that uses kb.KB as knowledge base.
    Should be sufficient to just implement __calcgrade__
    """
    def __init__(self,functions,KB=None):
        super(KBChooser,self).__init__(functions,KB or kb.KB())
        self.notes = kb.KB()
        self.notes.memory = {}

    def __getgrades__(self,*args,**kwargs):
        return [(f,self.notes.memory.get(f,0)) for f in self.possiblefunctions]

    def __aftercall__(self,choice,args,kwargs,result):
        self.notes.vars.f = choice
        self.notes.vars.oldresult = getattr(self.notes.values,'result',None)
        self.notes.vars.result = result
        self.notes.vars.args = args
        if self.notes.memory.has_key(choice):
            self.notes.memory[choice] = self.__calcgrade__(self.notes.memory[choice])
        else:
            self.notes.memory[choice] = self.__calcgrade__()

    def __calcgrade__(self,currentgrade=None):
        """Data to calculate grade is at self.notes.values"""
        raise NotImplementedError
