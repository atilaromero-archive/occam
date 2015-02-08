import choose
import functools

@choose.Choose
def recordmove(choosemove, getstate,getbest):
    def _recordmove():
        old = getstate()
        move = choosemove.getChoice()
        print move
        move()
        new = getstate()
        choose.Choose.memory[move] = (getbest(old,new) != old)
        return new
    return _recordmove
