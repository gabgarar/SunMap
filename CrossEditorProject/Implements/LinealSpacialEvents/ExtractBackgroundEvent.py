from Implements.Event import Event
import numpy as np
from Utils.utils import getMaxValue
import sunpy
import matplotlib.pyplot as plt

def insideLimbo(x, y, cx, cy, radius):
    a = (x - cx) ** 2
    b = (y - cy) ** 2
    d = np.sqrt(a + b)
    return d < radius  # True is in


def getRSun(map):
    return np.round((map.rsun_obs / map.scale[0]).value)



class ExtractBackgroundEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Background : Extract the background of a FITS image."

    def crop(self, img, radius):

        tt = img.dtype
        rg = getMaxValue(tt)
        cx, cy = img.shape

        X, Y = np.ogrid[:cx, :cy]
        outer_disk_mask = (X - cx / 2) ** 2 + (Y - cy / 2) ** 2 > radius ** 2
        ret = img.copy()
        ret[outer_disk_mask] = 0
        return ret

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if ss is not None:
            if mmap.getSeq():
                maps = [sunpy.map.Map(self.crop(elem.data, getRSun(elem)), elem.meta) for elem in ss]
                mmap.setMap(maps)
                #maps = [sunpy.map.Map(crop(elem.data, getRSun(elem)), elem.meta) for elem in ss]


            else:
                mmap.setMap(sunpy.map.Map(self.crop(mmap.getMap().data, mmap.getRSun()), ss.meta))
        else:
            print("You have to load a Fits image before.")
