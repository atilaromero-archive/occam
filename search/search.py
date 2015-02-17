class Search(object):
    def __init__(self,runner,isgoal,heuristic = None):
        self.runner = runner
        self.isgoal = isgoal
        if heuristic is None:
            heuristic = (lambda:0)
        self.heuristic = heuristic
    def __call__(self,state,goal):
        raise NotImplementedError

def listRunner(node):
    try:
        return enumerate(node)
    except TypeError:
        return []

def dictRunner(node):
    try:
        return node.iteritems()
    except AttributeError:
        return {}

def getItem(node,keyaddress):
    if len(keyaddress)>1:
        return getItem(node[keyaddress[0]],keyaddress[1:])
    else:
        return node[keyaddress[0]]
