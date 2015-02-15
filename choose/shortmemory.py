import kbChooser

class ShortMemory(kbChooser.KBChooser):
    def __calcgrade__(self,currentgrade=None):
        old=self.notes.values.oldresult
        new=self.notes.values.result
        #True=1, False=-1
        ret=int(self.KB.getbest(old,new) != old)*2 -1 
        return ret
