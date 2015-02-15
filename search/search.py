class Search(object):
    def __init__(self,runner,isgoal):
        self.runner = runner
        self.isgoal = isgoal
    def __call__(self,state,goal):
        raise NotImplementedError

class Runner(object):
    @staticmethod
    def getChildren(node):
        """Returns [(name,node), ...]"""
        raise NotImplementedError
        
class ListRunner(Runner):
    @staticmethod
    def getChildren(node):
        try:
            return enumerate(node)
        except TypeError:
            return []

class DictRunner(Runner):
    @staticmethod
    def getChildren(node):
        try:
            return node.iteritems()
        except AttributeError:
            return {}

class DeepFirstRecursive(Search):
    def __call__(self,name,node):
        if self.isgoal(name,node):
            return [name]
        for subname,subnode in self.runner.getChildren(node):
            result = self.__call__(subname,subnode)
            print 'result',result
            if not result is None:
                return [name]+result
        return None

def test(n=4):
    lst = [0,1,[0,[0,[0,1,[4,5,6]]]],2,[0,1,2,3,4],4]
    def isgoal(name,node):
        return node == n
    deep = DeepFirstRecursive(ListRunner,isgoal)
    return deep('start',lst)

def test2(n=4):
    dct = {0:{},1:{0:{0:{0:{},1:{4:{},5:6}}}},2:{0:1,2:3},4:0}
    def isgoal(name,node):
        return name == n
    deep = DeepFirstRecursive(DictRunner,isgoal)
    return deep('start',dct)
