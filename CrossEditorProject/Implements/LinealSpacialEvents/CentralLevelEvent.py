from Implements.Event import Event
import numpy as np
from Utils.utils import getMaxValue
import sunpy.map


def calcSigmod(rg, val, x):
    print(rg[1])
    inn = x / rg[1] - 0.5
    inSen = inn * val * np.pi
    par = 1 / (np.tan(val * np.pi / 2))
    parin = 1 + par * np.tan(inSen)
    ret = (rg[1] / 2) * parin
    return ret


class SigmodBrightEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Sigmod : Increase or decrease the values according to a sigmoid function."

    def Sigmod(self, val, imgData):
        tt = imgData.dtype
        rg = getMaxValue(tt)

        ret = calcSigmod(rg, val, imgData)
        ret = ret.astype(imgData.dtype)

        return ret

    def execute(self, mmap, comm):

        ss = mmap.getMap()
        if not comm:
            print(self.getDescription())
        elif ss is not None:
            val = float(comm.pop(0))

            if mmap.getSeq():
                maps = [sunpy.map.Map(self.Sigmod(val, elem.data), elem.meta) for elem in ss]
                mmap.setMap(maps)
            else:
                mmap.setMap(sunpy.map.Map(self.Sigmod(val, ss.data), ss.meta))

        else:
            print("You have to load a Fits image before.")
