#!/usr/bin/env python

import random
from equilibrium import A, B, C, D, E, F, piece

def rand(moves):
    """the most basic and memoryless strategy"""
    return random.choice(moves)

memory={}

def linear(moves):
    """assume moves produce a linear effect on obj"""
    return  random.choice(moves)

def choosemove(moves):
    for move in moves:
        if memory.has_key(move):
        
def makepredictions(memory):
    

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
