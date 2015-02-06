import random

def rnd(options):
    print 'rnd'
    return random.choice(options)
    
def first(options):
    print 'first'
    return options[0]

def plan(function):
    print '@plan',function.func_name
    def f(*args):
        print 'plan',function.func_name
        return plan.default(f.options)(*args)
    f.options=[function]
    return f
plan.default=rnd


def f1():
    print 1
    return 2

@plan
def f2():
    print 3
    return 4

f2.options.append(f1)
