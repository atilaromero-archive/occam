import kbChooser

class Points(kbChooser.KBChooser):
    def __calcgrade__(self,currentgrade=0):
        old=self.notes.values.oldresult
        new=self.notes.values.result
        #True=1, False=-1
        ret=int(self.KB.getbest(old,new) != old)*2 -1 
        return ret + currentgrade
