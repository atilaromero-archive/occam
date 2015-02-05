#!/usr/bin/env python
import random
import functools

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
        if len(f.options)==1:
            action = f.options[0]
        else:
            action = plan_action(f.options)
        result = eval_action(action,*args,**kwargs)
        recordresult(f.results,result,action,*args,**kwargs)
        return result
    f.options=[function]
    f.results={}
    return f

def loop(function):
    @functools.wraps(function)
    def f(*args,**kwargs):
        result = function(*args,**kwargs)
        while not is_solved():
            result = function(*args,**kwargs)
        return result
    return f

#TODO - for now, just use the first result
def is_solved():
    return True

def plan_action(options):
    return random.choose(options)

def eval_action(action,*args,**kwargs):
    return action(*args,**kwargs)

def recordresult(results,result,action,*args,**kwargs):
    pass
