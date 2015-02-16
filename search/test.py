from search import *
from breadthfirstrecursive import *
from depthfirstrecursive import *

def test(n=4):
    lst = [0,1,[0,[0,[0,1,[4,5,6]]]],2,[0,1,2,3,4],4]
    def isgoal(key,node):
        return node == n
    deep = DepthFirstRecursive(listRunner,isgoal)
    return deep('start',lst)

def test2(n=4):
    dct = {0:{},1:{0:{0:{0:{},1:{4:{},5:6}}}},2:{0:1,2:3},4:0}
    def isgoal(key,node):
        return key == n
    deep = DepthFirstRecursive(dictRunner,isgoal)
    return deep('start',dct)

def test3(n=4):
    lst2 = [0,
           [7],
           [1,[8]],
           [1,[2]],
           [6,
            [1,7,[3],[4]]],
           [7,[4]],
           8]
    def isgoal(key,node):
        return node == n
    deep = BreadthFirstRecursive(listRunner,isgoal)
    return deep('start',lst2),lst2

def test5(n=4):
    lst = [0,1,[0,[0,[0,1,[4,5,6]]]],2,[0,1,2,3,4],4]
    def isgoal(key,node):
        return node == n
    deep = DepthFirst(listRunner,isgoal)
    return deep('start',lst)

