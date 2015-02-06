#!/usr/bin/env python
import random
import functools

def fpass(*args,**kwargs):
    pass

def yes():
    return True

def perl(function):
    """
    Plan   - choose an action
    Eval   - run action
    Record - save result
    Loop   - try again until solved
    """
    @loop
    @functools.wraps(function)
    def f(*args,**kwargs):
        action = f.plan(f.options)
        result = action(*args,**kwargs)
        f.record(f.results,result,action,*args,**kwargs)
        return result
    f.options=[function]
    f.results={}
    f.solved=yes
    f.plan=getperlplan
    f.record=getperlrecord
    return f
perl.plan=random.choice
perl.record=fpass

def getperlplan(*args):
    return perl.plan(*args)

def getperlrecord(*args,**kwargs):
    return perl.record(*args,**kwargs)

def loop(function):
    @functools.wraps(function)
    def f(*args,**kwargs):
        result = function(*args,**kwargs)
        while not f.solved():
            result = function(*args,**kwargs)
        return result
    return f


def f1():
    return 2

@perl
def f2():
    return 4

f2.options.append(f1)
