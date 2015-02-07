#!/usr/bin/env python
import choose

@choose.Choose
def trial(function, getstate, goal):
    result = getstate()
    while not goal(result):
        function()
        result = getstate()
        print result
    return result
