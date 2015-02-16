class BreadthFirstRecursive(Search):
    def __call__(self,key,node,depth=None):
        print key,node,depth
        if depth==0:
            if self.isgoal(key,node):
                return [key]
            return None
        elif depth>0:
            hasdepth = False
            for subkey,subnode in self.runner(node):
                try:
                    result = self.__call__(subkey,subnode,depth-1)
                except IndexError:
                    pass
                else:
                    hasdepth = True
                    if not result is None:
                        return [key]+result
            if not hasdepth:
                raise IndexError
            return None
        else:
            try: 
                depth = 0
                while(True):
                    result = self.__call__(key,node,depth)
                    if not result is None:
                        return result
                    depth+=1
            except IndexError:
                return None
