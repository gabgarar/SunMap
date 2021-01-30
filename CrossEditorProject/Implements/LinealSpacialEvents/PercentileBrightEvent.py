from Implements.Event import Event
import numpy as np
import sunpy.map
from Utils.utils import getMaxValue


class PercentileBrightEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Percentile : All values below a percentile are passed to a value."

    def perc(self, per, val, imgData):
        img = imgData.copy()
        tt = img.dtype
        rg = getMaxValue(tt)

        pp = np.percentile(imgData, per)  # median in 50

        if rg[0] <= val <= rg[1]:
            img[img < pp] = val
            ret = img.astype(imgData.dtype)
            return ret
        else:
            print("The value must be within the range of the image format")

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if not comm or len(comm) < 2:
            print(self.getDescription())
        elif ss is not None:
            per = float(comm.pop(0))
            val = float(comm.pop(0))
            if 0 <= per <= 100:
                if mmap.getSeq():
                    maps = [sunpy.map.Map(self.perc(per, val, elem.data), elem.meta) for elem in ss]
                    mmap.setMap(maps)

                else:
                    mmap.setMap(sunpy.map.Map(self.perc(per, val, ss.data), ss.meta))
            else:
                print("The percentile range has to be between 0 and 100")
        else:
            print("You have to load a Fits image before.")
