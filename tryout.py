#!/usr/bin/env python

import random
from equilibrium import A, B, C, D, E, F, piece

def rand(moves,obj,goal):
    """the most basic and memoryless strategy"""
    while obj.value != goal:
        print random.choice(moves)()

def test():
    rand([A,B,C,D,E,F],piece,0)
