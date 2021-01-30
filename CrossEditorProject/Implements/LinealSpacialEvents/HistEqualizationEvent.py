from Implements.Event import Event
from skimage import exposure
from skimage.morphology import disk
from skimage.filters import rank
from Utils.utils import cast
import numpy as np
from numba import jit, cuda
from timeit import default_timer as timer
import sunpy


class HistEqualizationEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Equalization : Equalizes a FITS image."

    def equ(self, imgData, first, val):
        tt = imgData.dtype

        ret = None
        if first == "global":
            im = exposure.equalize_hist(imgData)
            ret = cast(im, tt)
        elif first == "contrast":
            ret = self.contrast(imgData, val)
        elif first == "adapt":
            ret = cast(self.adapt(imgData, val), tt)
        elif first == "rank":
            start = timer()
            ret = self.rank(imgData, val)
            print("with GPU:", timer() - start)

        return ret

    @jit
    def contrast(self, imgData, p):
        pinf, psup = np.percentile(imgData, (100 - p, p))
        return exposure.rescale_intensity(imgData, in_range=(pinf, psup))

    @jit
    def adapt(self, imgData, c):
        return exposure.equalize_adapthist(imgData, clip_limit=c)  # 0.03

    @jit
    def rank(self, imgData, c):
        return rank.equalize(imgData, selem=disk(c))

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        first = comm.pop(0)

        if len(comm) != 0:
            val = float(comm.pop(0))
        else:
            val = None
        if ss is not None:

            if mmap.getSeq():
                maps = [sunpy.map.Map(self.equ(elem.data, first, val), elem.meta) for elem in ss]
                mmap.setMap(maps)
            else:
                mmap.setMap(sunpy.map.Map(self.equ(ss.data, first, val), ss.meta))

        else:
            print("You have to load a Fits image before.")
