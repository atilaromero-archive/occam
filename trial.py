#!/usr/bin/env python

import choose
from equilibrium import A, B, C, D, E, F, piece

memory={}

@choose.choose
def trial(function, goal):
    result = None
    while not goal():
        result = function()
    return result

def test():
    while obj.value != goal:
        strategy = None
        while strategy == None:
            strategy = rand([rand,linear])
        state = obj.value
        move = strategy([A,B,C,D,E,F])
        result = move()
        if not memory.has_key(move):
            memory[move]=[]
        memory[move].append((state,move,result))

test()
