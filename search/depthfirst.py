import search

class DepthFirst(search.Search):
    def __call__(self,node):
        queue = {}
        queue[0] = [[k] for k,v in self.runner(node)]
        while queue:
            print queue
            priority = max(queue.keys())
            itemk = queue[priority].pop(0)
            itemv = search.getItem(node,itemk)
            if not queue[priority]:
                del queue[priority]
            if self.isgoal(itemk,itemv):
                return (itemk,itemv)
            else:
                newitems = [itemk+[k] for k,v in self.runner(itemv)]
                if newitems:
                    queue[priority+1] = queue.get(priority+1,[]) + newitems
        return None
                
