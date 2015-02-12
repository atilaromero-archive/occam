import sympy

class KB(object):
    def __init__(self):
        self.statements = []
        self.vars = varsVault(self)
        self.values = AttrDict()
        for x in sympy.symbols('result f args goal'.split()):
            setattr(self.vars,x.name,x)
        self.vars.result = self.vars.f(self.vars.args)
        
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class varsVault(object):
    def __init__(self, parentKB):
        self._parentKB = parentKB
    def __setattr__(self,key,value):
        #if attr is a symbol
        if hasattr(self,key) and isinstance(getattr(self,key),sympy.Basic):
            if isinstance(value,sympy.Basic):
                self._parentKB.statements.append(sympy.Eq(getattr(self,key),value))
            else:
                setattr(self._parentKB.values,key,value)
        else:
            super(varsVault,self).__setattr__(key,value)
