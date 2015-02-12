import choose
import sympy
from equilibrium import A,B,C,D,E,F,piece

def quicksort(l):
    print 'quicksort'
    if len(l)<=1:
        return l[:1]
    else:
        g=[x for x in l[1:] if x>l[0]]
        m=[x for x in l[1:] if x<=l[0]]
        return quicksort(m)+l[:1]+quicksort(g)

def bubblesort(l):
    print 'bubblesort'
    r=l[:]
    for p in range(len(r)-1,0,-1):
        for i in range(p):
            if r[i]>r[i+1]:
                r[i],r[i+1] = r[i+1],r[i]
    return r

def test():
    mysort = choose.Base([quicksort,bubblesort])
    print mysort(list('784268074'))

def f1():
    print 1

def f2():
    print 2

def f3():
    print 3

def test2():
    myf = choose.Base([f1,f2])
    myf.possiblefunctions.append(f3)
    for x in range(6):
        myf()

def near_zero(x):
    return -1 < x and x < 1

def bestnum(x,y):
    try:
        if abs(x)<abs(y):
            return x
        else:
            return y
    except:
        return y

def testsm():
    move = choose.ShortMemory([A,B,C,D,E,F])
    move.KB.getbest = bestnum
    move.KB.vars.goal = sympy.Eq(move.KB.vars.result,0)
    for x in range(10):
        move()
        print move.KB.values.f,move.KB.values.result
    return move
