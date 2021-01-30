from scipy import ndimage
from scipy.ndimage import gaussian_filter
from skimage.restoration import denoise_wavelet, estimate_sigma

from Implements.Event import Event
from skimage import exposure, img_as_float
from skimage.morphology import disk, reconstruction
from numba import jit, cuda
from timeit import default_timer as timer
from Utils.utils import cast, getMaxValue, rescale
import numpy as np
import sunpy


class BlurEvent(Event):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Blur: Increase or decrease brightness of a FITS image."

    def equ(self, imgData, comm):
        tt = imgData.dtype
        ret = None
        first = comm.pop(0)

        if first == "gauss":
            val = float(comm.pop(0))
            if val is not None:
                ret = ndimage.gaussian_filter(imgData, val)

        elif first == "median":
            val = int(float(comm.pop(0)))
            if val is not None:
                ret = ndimage.median_filter(imgData, val)
        return ret

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if ss is not None and comm is not None:
            if mmap.getSeq():
                maps = [sunpy.map.Map(self.equ(elem.data, comm), elem.meta) for elem in ss]
                mmap.setMap(maps)
            else:
                mmap.setMap(sunpy.map.Map(self.equ(ss.data, comm), ss.meta))

        else:
            print("You have to load a Fits image before.")


