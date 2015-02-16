class DepthFirstRecursive(Search):
    def __call__(self,key,node):
        if self.isgoal(key,node):
            return [key]
        for subkey,subnode in self.runner(node):
            result = self.__call__(subkey,subnode)
            if not result is None:
                return [key]+result
        return None
