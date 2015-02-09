#!/usr/bin/env python
import choose
import goodbad

def loop(func,KB):
    result = KB.getstate()
    print result
    while not KB.goal(result):
        func()
        result = KB.getstate()
        print result
    return result
