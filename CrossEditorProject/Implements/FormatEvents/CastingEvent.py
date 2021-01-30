from skimage.util import *

from Implements.Event import Event


class CastingEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Casting : Casting a FITS image "

    def execute(self, mmap, comm):
        if not comm:
            print(self.getDescription())
        elif len(comm) > 0 and mmap.getImg() is not None:
            casted = None
            inter = mmap.getImg().dtype
            val = str(comm.pop(0))

            if inter != val and val == "float64":
                casted = img_as_float64(mmap.getImg())
            elif inter != val and val == "float":
                casted = img_as_float(mmap.getImg())
            elif inter != val and val == "uint8":
                casted = img_as_ubyte(mmap.getImg())
            elif inter != val and val == "uint16":
                casted = img_as_uint(mmap.getImg())

            mmap.setIsUpdate(True)
            mmap.setImg(casted)
            mmap.changeNormalized()

        else:
            print("You have to load the file fits before")
