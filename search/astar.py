import search

class AStar(search.Search):
    def __call__(self,node):
        queue = {}
        self.addtoqueue(queue,0,[],node)
        while queue:
            print queue
            priority = min(queue.keys())
            prevcost,itemk = queue[priority].pop(0)
            stepcost,itemv = getItem(node,itemk)
            if self.isgoal(itemk,itemv):
                return (itemk,itemv)
            if not queue[priority]:
                del queue[priority]
            self.addtoqueue(queue,prevcost,itemk,itemv)
        return None

    def addtoqueue(self,queue,prevcost,partialpath,node):
        for k,(stepcost,v) in self.runner(node):
            priority = prevcost+stepcost+self.heuristic(k,v)
            queue[priority] = queue.get(priority,[]) + [(prevcost+stepcost,partialpath+[k])]

def getItem(node,keyaddress):
    if len(keyaddress)>1:
        return getItem(node[keyaddress[0]][1],keyaddress[1:])
    else:
        return node[keyaddress[0]]
        
                
g = {}
c = {'G':(3,g)}
b = {'C':(2,c)}
a = {'B':(2,b),'C':(5,c),'G':(12,g)}
s = {'A':(1,a),'B':(4,b)}

def isgoal(k,v):
    return k[-1] == 'G'

def heuristic(k,v):
    tb = {'S':7,
          'A':6,
          'B':2,
          'C':1,
          'G':0,
      }
    return tb[k]

print AStar(search.dictRunner,isgoal,heuristic)({'S':(0,s)})
