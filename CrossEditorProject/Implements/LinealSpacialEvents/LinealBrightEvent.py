from scipy.ndimage import gaussian_filter
from Implements.Event import Event
from skimage import exposure, img_as_float
from skimage.morphology import reconstruction
from numba import jit
from Utils.utils import cast, getMaxValue, rescale
import numpy as np
import sunpy


class LinealBrightEvent(Event):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Bright : Increase or decrease brightness of a FITS image."

    @jit
    def linea(self, imgData, val, tt):
        imgData = rescale(imgData)
        max = np.max(imgData) * 0.01 * val
        rg = getMaxValue(tt)
        if val > 0:
            im = np.where(imgData + max < rg[1], imgData + max, rg[1])
        else:
            im = np.where(imgData + max > rg[0], imgData + max, rg[0])
        return im

    def equ(self, imgData, first, val):
        tt = imgData.dtype
        ret = None

        print("LINEAL BRIGHT EVENT")
        if first == "lineal":
            print(f"Por último, val vale : {val}")
            if val is not None:
                ret = cast(self.linea(imgData, val, tt), tt)

        elif first == "gamma":
            if val is not None:
                ret = exposure.adjust_gamma(imgData, val)

        elif first == "log":
            if val is not None:
                ret = exposure.adjust_log(imgData, val)

        elif first == "regional":
            if val is not None:
                image = img_as_float(imgData)
                image = gaussian_filter(image, val)

                seed = np.copy(image)
                seed[1:-1, 1:-1] = image.min()
                mask = image

                dilated = reconstruction(seed, mask, method='dilation')
                im = image - dilated
                ret = im

        elif first == "filled":  # Rellenar los huecos
            if val is not None:
                image = img_as_float(imgData)
                image = gaussian_filter(image, val)

                seed = np.copy(image)
                seed[1:-1, 1:-1] = image.max()
                mask = image

                filled = reconstruction(seed, mask, method='erosion')
                #
                ret = filled

        return ret

    def execute(self, mmap, comm):
        ss = mmap.getMap()
        if ss is not None and comm is not None:
            first = comm.pop(0)
            val = float(comm.pop(0))
            if mmap.getSeq():
                maps = [sunpy.map.Map(self.equ(elem.data, first, val), elem.meta) for elem in ss]
                mmap.setMap(maps)
            else:
                mmap.setMap(sunpy.map.Map(self.equ(ss.data, first, val), ss.meta))

        else:
            print("You have to load a Fits image before.")


