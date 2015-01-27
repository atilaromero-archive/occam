#!/usr/bin/env python

import random

class Obj:
    """Something to store a value between function calls"""
    def __init__(self):
        self.value=random.random()*100
    def __repr__(self):
        return repr(self.value)

piece=Obj()

def move(obj,x,error):
    obj.value+=(x+random.random()*error)
    return obj.value
    
#the possible moves
def A():
    return move(piece,10,1)

def B():
    return move(piece,-10,1)

def C():
    return move(piece,3,1)

def D():
    return move(piece,-2,1)

def E():
    return move(piece,10,3)

def F():
    return move(piece,-1,1)

#the problem: make piece reach 0 using moves ABCDEF without knowing at first what these moves do
problem=[[A,B,C,D,E,F],piece,0]
