#!/usr/bin/env python
import choose

@choose.Choose
@choose.need(['getstate','goal'])
def loop(func,intel):
    result = intel.getstate()
    print result
    while not intel.goal(result):
        func(intel=intel)
        result = intel.getstate()
        print result
    return result
