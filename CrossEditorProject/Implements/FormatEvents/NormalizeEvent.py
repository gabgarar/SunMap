import numpy as np

from Implements.Event import Event


class NormalizeEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Normalize : Normalize a FITS image "

    def execute(self, mmap, comm):
        try:
            if not comm:
                print(self.getDescription())
            elif mmap.getImg() is not None:
                val = float(comm.pop(0))
                iMax = np.max(mmap.getImg())
                iMin = np.min(mmap.getImg())
                norm = val * (mmap.getImg() - iMin) / (iMax - iMin)

                mmap.setImg(norm)
                mmap.changeNormalized()
                mmap.setIsUpdate(True)
            elif mmap.getImg() is None:
                print("You have to load the file fits before")
        except ValueError:
            print("You have to enter a number as an argument.")
