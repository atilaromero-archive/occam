import sympy

class KB(object):
    def __init__(self):
        self.statements = []
        self.vars = varsVault(self)
        self.values = AttrDict()
        for x in sympy.symbols('oldresult result f args goal'.split()):
            setattr(self.vars,x.name,x)
        self.vars.result = self.vars.f(self.vars.args)
        
class AttrDict(dict):
    """dict whose keys are accessible as attributes"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class varsVault(object):
    """Attributes in varsVault are treated in a peculiar way:

    * if key is not a sympy symbol, nothing changes
    > myvault.notsymbol = something
    call to regular __setattr__
    
    * if key is a symbol and is receiving another symbol,
    we assume '=' is intended as mathematical '=', not assignment
    > myvault.symbolA = symbolB
    _parentKB receives a new statement: Eq(symbolA,symbolB)
    
    * if key is a symbol but is receiving something that is NOT a symbol,
    we assume we are trying to register the current value of symbol
    > myvault.symbolA = 3 
    we store the current value of symbolA in _parentKB.values
    """
    def __init__(self, parentKB):
        self._parentKB = parentKB
    def __setattr__(self,key,value):
        #if attr is a symbol
        if hasattr(self,key) and isinstance(getattr(self,key),sympy.Basic):
            if isinstance(value,sympy.Basic):
                # myvault.symbolA = symbolB
                self._parentKB.statements.append(sympy.Eq(getattr(self,key),value))
            else:
                # myvault.symbolA = 3
                setattr(self._parentKB.values,key,value)
        else:
            # myvault.notsymbol = something
            super(varsVault,self).__setattr__(key,value)
