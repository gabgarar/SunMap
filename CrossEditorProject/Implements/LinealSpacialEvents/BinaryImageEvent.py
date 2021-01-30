from Implements.Event import Event
import numpy as np
import sunpy.map

from Utils.utils import getMaxValue


class BinaryImageEvent(Event):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Binary : Binary filter. "

    def bin(self, val, imgData):
        pp = np.percentile(imgData, val)
        img = imgData.copy()
        dd = getMaxValue(img.dtype)
        img[img < pp] = dd[0]
        img[img >= pp] = dd[1]

        return img

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if not comm:
            print(self.getDescription())
        elif ss is not None:
            val = float(comm.pop(0))

            if 0 <= val <= 100:
                if mmap.getSeq():
                    maps = [sunpy.map.Map(self.bin(val, elem.data), elem.meta) for elem in ss]
                    mmap.setMap(maps)
                else:
                    mmap.setMap(sunpy.map.Map(self.bin(val, ss.data), ss.meta))
            else:
                print("The percentile range has to be between 0 and 100")
