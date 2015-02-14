import basernd
from .. import kb

class ModeratorFactory(object):
    def __init__(self, choosers):
        self.choosers = choosers
    def __call__(self, possiblefunctions):
        return Moderator(choosers,possiblefunctions)

class Moderator(basernd.BaseRnd):
    def __init__(self, choosers, possiblefunctions):
        KB = kb.KB()
        super(Moderator,self).__init__(possiblefunctions,KB)
        self.choosers = choosers
    def __getgrades__(self, *args, **kwargs):
        




