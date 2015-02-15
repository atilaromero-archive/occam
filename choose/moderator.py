import random
import base
import kb

class ModeratorFactory(object):
    def __init__(self, moderator,choosers):
        self.moderator = moderator
        self.choosers = choosers
    def __call__(self, possiblefunctions):
        modinstance = self.moderator([])
        for c in self.choosers:
            modinstance.possiblefunctions.append(c(possiblefunctions,KB=modinstance.KB))
        return modinstance
