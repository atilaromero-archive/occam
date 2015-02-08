#!/usr/bin/env python
import choose

@choose.Choose
def loop(recordmove, getstate, goal):
    result = getstate()
    print result
    while not goal(result):
        result = recordmove()
        print result
    return result
