class Search(object):
    def __init__(self,runner,isgoal):
        self.runner = runner
        self.isgoal = isgoal
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
