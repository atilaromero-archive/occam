import sympy

class KB(object):
    def __init__(self):
        self.content = []
        for x in sympy.symbols('result args f goal'.split()):
            self.content.append(x)
            setattr(self,x.name,x)
        self.result = self.f(self.args)
        self.values = {}
    def __setattr__(self,key,value):
        if hasattr(self,key) and isinstance(getattr(self,key),sympy.Symbol):
            self.content.append(sympy.Eq(getattr(self,key),value))
        else:
            super(KB,self).__setattr__(key,value)
        
