import random

def perl(function):
    def f(*args):
        return plan(f.options)
    f.options=[function]
    return f

def plan(function):
    print 'plan',function.func_name
    def f(*args):
        print 'plan f',function.func_name
        return random.choice(f.options)(*args)
    f.options=[function]
    return f

def first(function):
    print 'first',function.func_name
    def f(*args):
        print 'first f',function.func_name
        return f.options[0](*args)
    f.options=[function]
    return f

plan2 = plan(plan)
plan2.options.append(first)
        
def f1():
    print 1
    return 2

@plan
def f2():
    print 3
    return 4

f2.options.append(f1)
